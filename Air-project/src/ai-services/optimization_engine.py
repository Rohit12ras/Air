"""
AI Travel Optimization Engine
Provides intelligent cost and carbon optimization for travel bookings
"""

from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime, timedelta
import numpy as np


@dataclass
class TravelOption:
    """Represents a travel option with all relevant data"""
    option_id: str
    transport_type: str  # flight, train, car, bus
    origin: str
    destination: str
    departure: datetime
    arrival: datetime
    price_usd: float
    co2_kg: float
    carrier: str
    travel_class: str = "economy"
    amenities: List[str] = None
    comfort_score: float = 7.0


@dataclass
class OptimizationPreferences:
    """User preferences for travel optimization"""
    max_budget: Optional[float] = None
    max_co2: Optional[float] = None
    max_duration_hours: Optional[float] = None
    priorities: List[str] = None  # ['cost', 'carbon', 'time', 'comfort']
    preferred_carriers: List[str] = None
    avoid_carriers: List[str] = None
    min_comfort_score: float = 6.0


@dataclass
class OptimizationResult:
    """Result of AI optimization"""
    recommended_option: TravelOption
    alternatives: List[TravelOption]
    savings: Dict[str, float]
    ai_score: float
    reasoning: str
    confidence: float


class CarbonCalculator:
    """Calculate CO2 emissions for different transport modes"""

    # Emission factors (kg CO2 per km)
    EMISSION_FACTORS = {
        'flight_economy': 0.115,
        'flight_premium_economy': 0.184,
        'flight_business': 0.334,
        'flight_first': 0.460,
        'train_electric_highspeed': 0.014,
        'train_electric_regional': 0.028,
        'train_diesel': 0.041,
        'car_electric': 0.0,
        'car_hybrid': 0.08,
        'car_compact': 0.12,
        'car_midsize': 0.15,
        'car_suv': 0.20,
        'car_luxury': 0.25,
        'bus_coach': 0.027,
    }

    # Aircraft type multipliers
    AIRCRAFT_FACTORS = {
        'narrow_body': 1.0,   # A320, 737
        'wide_body': 0.85,    # A330, 777, 787
        'regional': 1.2,      # CRJ, ERJ
        'electric': 0.1,
    }

    # Hotel emissions (kg CO2 per night)
    HOTEL_EMISSIONS = {
        'standard': 20.0,
        'suite': 30.0,
        'villa': 40.0,
        'leed_platinum': 10.0,
        'leed_gold': 14.0,
        'green_certified': 17.0,
    }

    @classmethod
    def calculate_flight_emissions(
        cls,
        distance_km: float,
        travel_class: str = 'economy',
        aircraft_type: str = 'narrow_body'
    ) -> float:
        """Calculate CO2 emissions for a flight"""
        base_key = f'flight_{travel_class}'
        emission_factor = cls.EMISSION_FACTORS.get(base_key, 0.115)
        aircraft_multiplier = cls.AIRCRAFT_FACTORS.get(aircraft_type, 1.0)

        co2_kg = distance_km * emission_factor * aircraft_multiplier

        # Add radiative forcing factor (flights have 2-4x impact at altitude)
        co2_kg *= 2.0

        return round(co2_kg, 2)

    @classmethod
    def calculate_train_emissions(
        cls,
        distance_km: float,
        train_type: str = 'electric_highspeed'
    ) -> float:
        """Calculate CO2 emissions for a train journey"""
        key = f'train_{train_type}'
        emission_factor = cls.EMISSION_FACTORS.get(key, 0.028)
        return round(distance_km * emission_factor, 2)

    @classmethod
    def calculate_car_emissions(
        cls,
        distance_km: float,
        vehicle_type: str = 'midsize'
    ) -> float:
        """Calculate CO2 emissions for a car rental"""
        key = f'car_{vehicle_type}'
        emission_factor = cls.EMISSION_FACTORS.get(key, 0.15)
        return round(distance_km * emission_factor, 2)

    @classmethod
    def calculate_hotel_emissions(
        cls,
        nights: int,
        room_type: str = 'standard',
        efficiency_rating: str = None
    ) -> float:
        """Calculate CO2 emissions for hotel stay"""
        if efficiency_rating:
            base_emission = cls.HOTEL_EMISSIONS.get(efficiency_rating, 20.0)
        else:
            base_emission = cls.HOTEL_EMISSIONS.get(room_type, 20.0)

        return round(nights * base_emission, 2)


class AIOptimizationEngine:
    """AI-powered travel optimization engine"""

    def __init__(self):
        self.carbon_calculator = CarbonCalculator()

    def optimize_route(
        self,
        options: List[TravelOption],
        preferences: OptimizationPreferences
    ) -> OptimizationResult:
        """
        Find optimal travel option based on cost, carbon, and preferences

        Uses multi-objective optimization with weighted scoring
        """
        if not options:
            raise ValueError("No travel options provided")

        # Filter options based on hard constraints
        filtered_options = self._apply_constraints(options, preferences)

        if not filtered_options:
            # If no options meet constraints, relax them
            filtered_options = options

        # Calculate scores for each option
        scored_options = []
        for option in filtered_options:
            score = self._calculate_option_score(option, preferences)
            scored_options.append((score, option))

        # Sort by score (highest first)
        scored_options.sort(key=lambda x: x[0], reverse=True)

        # Best option
        best_score, best_option = scored_options[0]

        # Alternative options
        alternatives = [opt for score, opt in scored_options[1:4]]

        # Calculate savings vs most expensive option
        savings = self._calculate_savings(best_option, options)

        # Generate reasoning
        reasoning = self._generate_reasoning(
            best_option,
            alternatives,
            preferences,
            savings
        )

        return OptimizationResult(
            recommended_option=best_option,
            alternatives=alternatives,
            savings=savings,
            ai_score=best_score,
            reasoning=reasoning,
            confidence=self._calculate_confidence(scored_options)
        )

    def _apply_constraints(
        self,
        options: List[TravelOption],
        preferences: OptimizationPreferences
    ) -> List[TravelOption]:
        """Filter options based on hard constraints"""
        filtered = options

        if preferences.max_budget:
            filtered = [o for o in filtered if o.price_usd <= preferences.max_budget]

        if preferences.max_co2:
            filtered = [o for o in filtered if o.co2_kg <= preferences.max_co2]

        if preferences.max_duration_hours:
            filtered = [
                o for o in filtered
                if (o.arrival - o.departure).total_seconds() / 3600 <= preferences.max_duration_hours
            ]

        if preferences.min_comfort_score:
            filtered = [o for o in filtered if o.comfort_score >= preferences.min_comfort_score]

        if preferences.avoid_carriers:
            filtered = [o for o in filtered if o.carrier not in preferences.avoid_carriers]

        return filtered

    def _calculate_option_score(
        self,
        option: TravelOption,
        preferences: OptimizationPreferences
    ) -> float:
        """
        Calculate weighted score for a travel option
        Score range: 0-10 (higher is better)
        """
        # Default priority weights
        weights = {
            'cost': 0.35,
            'carbon': 0.25,
            'time': 0.20,
            'comfort': 0.20
        }

        # Adjust weights based on user priorities
        if preferences.priorities:
            total_priority = len(preferences.priorities)
            for i, priority in enumerate(preferences.priorities):
                # First priority gets highest weight
                weight = (total_priority - i) / sum(range(1, total_priority + 1))
                weights[priority] = weight

        # Normalize scores (0-10 scale)
        cost_score = self._score_cost(option.price_usd)
        carbon_score = self._score_carbon(option.co2_kg)
        time_score = self._score_duration(option.departure, option.arrival)
        comfort_score = option.comfort_score

        # Weighted sum
        total_score = (
            weights['cost'] * cost_score +
            weights['carbon'] * carbon_score +
            weights['time'] * time_score +
            weights['comfort'] * comfort_score
        )

        # Bonus for preferred carriers
        if preferences.preferred_carriers and option.carrier in preferences.preferred_carriers:
            total_score += 0.5

        return round(total_score, 2)

    def _score_cost(self, price: float) -> float:
        """Score based on cost (lower is better)"""
        # Assume reasonable range: $100-$5000
        if price <= 100:
            return 10.0
        elif price >= 5000:
            return 0.0
        else:
            # Linear inverse scaling
            return 10.0 - ((price - 100) / 4900 * 10.0)

    def _score_carbon(self, co2_kg: float) -> float:
        """Score based on carbon emissions (lower is better)"""
        # Assume reasonable range: 0-2000 kg CO2
        if co2_kg <= 0:
            return 10.0
        elif co2_kg >= 2000:
            return 0.0
        else:
            # Linear inverse scaling
            return 10.0 - (co2_kg / 2000 * 10.0)

    def _score_duration(self, departure: datetime, arrival: datetime) -> float:
        """Score based on travel duration (shorter is better)"""
        duration_hours = (arrival - departure).total_seconds() / 3600

        # Assume reasonable range: 1-20 hours
        if duration_hours <= 1:
            return 10.0
        elif duration_hours >= 20:
            return 0.0
        else:
            # Linear inverse scaling
            return 10.0 - ((duration_hours - 1) / 19 * 10.0)

    def _calculate_savings(
        self,
        chosen_option: TravelOption,
        all_options: List[TravelOption]
    ) -> Dict[str, float]:
        """Calculate savings compared to alternatives"""
        if not all_options:
            return {}

        # Find most expensive option (typical choice without AI)
        avg_price = np.mean([o.price_usd for o in all_options])
        max_price = max([o.price_usd for o in all_options])
        avg_co2 = np.mean([o.co2_kg for o in all_options])

        return {
            'cost_saved_usd': round(max_price - chosen_option.price_usd, 2),
            'cost_saved_percentage': round((max_price - chosen_option.price_usd) / max_price * 100, 1),
            'co2_saved_kg': round(avg_co2 - chosen_option.co2_kg, 2),
            'co2_saved_percentage': round((avg_co2 - chosen_option.co2_kg) / avg_co2 * 100, 1),
        }

    def _generate_reasoning(
        self,
        chosen: TravelOption,
        alternatives: List[TravelOption],
        preferences: OptimizationPreferences,
        savings: Dict[str, float]
    ) -> str:
        """Generate human-readable explanation for the recommendation"""
        reasons = []

        # Cost savings
        if savings.get('cost_saved_usd', 0) > 50:
            reasons.append(
                f"Saves ${savings['cost_saved_usd']:.0f} "
                f"({savings['cost_saved_percentage']:.0f}%) compared to typical choice"
            )

        # Carbon savings
        if savings.get('co2_saved_kg', 0) > 100:
            reasons.append(
                f"Reduces carbon footprint by {savings['co2_saved_kg']:.0f} kg CO2 "
                f"({savings['co2_saved_percentage']:.0f}%)"
            )

        # Transport mode benefits
        if chosen.transport_type == 'train':
            reasons.append(
                "Train offers better value with city-center to city-center convenience "
                "and lower environmental impact"
            )
        elif chosen.transport_type == 'flight' and chosen.travel_class == 'economy':
            reasons.append(
                "Economy class provides the best cost-per-mile while maintaining comfort"
            )

        # Comfort
        if chosen.comfort_score >= 8.0:
            reasons.append(f"High comfort rating: {chosen.comfort_score}/10")

        if not reasons:
            reasons.append("Best overall value considering cost, time, and environmental impact")

        return ". ".join(reasons) + "."

    def _calculate_confidence(self, scored_options: List[Tuple[float, TravelOption]]) -> float:
        """Calculate confidence in the recommendation (0-1)"""
        if len(scored_options) < 2:
            return 1.0

        # Confidence based on score gap between best and second-best
        best_score = scored_options[0][0]
        second_score = scored_options[1][0]

        score_gap = best_score - second_score

        # Larger gap = higher confidence
        # Gap of 2.0+ = very confident (0.95)
        # Gap of 0.5 = moderate confidence (0.70)
        # Gap of 0.1 = low confidence (0.60)

        if score_gap >= 2.0:
            return 0.95
        elif score_gap >= 1.0:
            return 0.85
        elif score_gap >= 0.5:
            return 0.75
        else:
            return 0.65

    def suggest_train_alternative(
        self,
        origin: str,
        destination: str,
        flight_option: TravelOption
    ) -> Optional[OptimizationResult]:
        """
        Check if train is better alternative for short routes
        Triggers for routes <500km or <4 hours flight time
        """
        # Calculate approximate distance from flight time
        flight_duration = (flight_option.arrival - flight_option.departure).total_seconds() / 3600

        # Only suggest train for short routes
        if flight_duration > 4:
            return None

        # Mock train option (in production, query real train API)
        train_duration_hours = flight_duration * 1.2  # Assume train 20% slower

        train_option = TravelOption(
            option_id="train_alternative",
            transport_type="train",
            origin=origin,
            destination=destination,
            departure=flight_option.departure,
            arrival=flight_option.departure + timedelta(hours=train_duration_hours),
            price_usd=flight_option.price_usd * 0.4,  # Trains typically 40-60% cheaper
            co2_kg=flight_option.co2_kg * 0.05,  # Trains 95% less emissions
            carrier="High-Speed Rail",
            travel_class="standard",
            comfort_score=8.5
        )

        savings = {
            'cost_saved_usd': flight_option.price_usd - train_option.price_usd,
            'cost_saved_percentage': ((flight_option.price_usd - train_option.price_usd) / flight_option.price_usd) * 100,
            'co2_saved_kg': flight_option.co2_kg - train_option.co2_kg,
            'co2_saved_percentage': ((flight_option.co2_kg - train_option.co2_kg) / flight_option.co2_kg) * 100,
        }

        reasoning = (
            f"Train is recommended for this route. "
            f"Saves ${savings['cost_saved_usd']:.0f} ({savings['cost_saved_percentage']:.0f}%) "
            f"and {savings['co2_saved_kg']:.0f} kg CO2 ({savings['co2_saved_percentage']:.0f}%). "
            f"Only {abs(train_duration_hours - flight_duration):.1f} hours difference when including airport time. "
            f"Travel city-center to city-center with no security lines."
        )

        return OptimizationResult(
            recommended_option=train_option,
            alternatives=[flight_option],
            savings=savings,
            ai_score=9.2,
            reasoning=reasoning,
            confidence=0.90
        )


# Example usage
if __name__ == "__main__":
    # Sample flight options
    options = [
        TravelOption(
            option_id="flight_business",
            transport_type="flight",
            origin="NYC",
            destination="LON",
            departure=datetime(2026, 4, 15, 18, 0),
            arrival=datetime(2026, 4, 16, 6, 30),
            price_usd=4200,
            co2_kg=1850,
            carrier="British Airways",
            travel_class="business",
            comfort_score=9.5
        ),
        TravelOption(
            option_id="flight_premium_economy",
            transport_type="flight",
            origin="NYC",
            destination="LON",
            departure=datetime(2026, 4, 15, 18, 0),
            arrival=datetime(2026, 4, 16, 6, 30),
            price_usd=2300,
            co2_kg=720,
            carrier="British Airways",
            travel_class="premium_economy",
            comfort_score=8.5
        ),
        TravelOption(
            option_id="flight_economy",
            transport_type="flight",
            origin="NYC",
            destination="LON",
            departure=datetime(2026, 4, 15, 18, 0),
            arrival=datetime(2026, 4, 16, 6, 30),
            price_usd=850,
            co2_kg=920,
            carrier="British Airways",
            travel_class="economy",
            comfort_score=7.0
        ),
    ]

    preferences = OptimizationPreferences(
        priorities=['cost', 'carbon', 'comfort'],
        min_comfort_score=7.0
    )

    engine = AIOptimizationEngine()
    result = engine.optimize_route(options, preferences)

    print(f"AI Recommended Option: {result.recommended_option.option_id}")
    print(f"Price: ${result.recommended_option.price_usd}")
    print(f"CO2: {result.recommended_option.co2_kg} kg")
    print(f"AI Score: {result.ai_score}/10")
    print(f"Confidence: {result.confidence * 100:.0f}%")
    print(f"\nReasoning: {result.reasoning}")
    print(f"\nSavings:")
    print(f"  Cost: ${result.savings['cost_saved_usd']:.0f} ({result.savings['cost_saved_percentage']:.0f}%)")
    print(f"  CO2: {result.savings['co2_saved_kg']:.0f} kg ({result.savings['co2_saved_percentage']:.0f}%)")
