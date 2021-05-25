# Ocean City Master List

This is a list of activities for Ocean City 2021

## Master List
- Beach
- Fenwick St. Park
- Northside Park
- Jolly Rogers Water Park
- Jolly Rogers Go Carts
- Jolly Rogers Amusement
- Boardwalk Shopping
- Boardwalk Cycling
- Boardwalk Arcades
- City Cycling
- Neighborhood Pool
- Mini Golf
- Grand Prix Go Carts
- Driving Range
- Climbing Gym
- Gym
- Seacrets
- Movie Theatre
- Parasailing
- Water Skiing
- Asseteague St. Park
- Visit Nonnie

For more information on the details of each activities, there are JSON and CSV documents containing more information on each activity.

## Data Dictionary
| Field Name     | Type | Description |
| -------------- | ---- | ----------- |
| activity_name  | str  | Name of the activity |
| req_weather    | int  | Worst acceptable weather condition: 0 = all weather conditions, 1 = no rain, 2 = sun required |
| req_outdoors   | bool | Denotes if the activity is only available outdoors |
| is_walkable    | bool | Denotes if the activity can be reached without a vehicle |
| drive_distance | int  | Denotes the approximate drive time in minutes |
| covid_score    | int  | Estimated COVID safety: 0 = outdoors and not crowded, 1 = outdoors and crowded or indoors and not crowded, 2 = indoors and crowded or poor ventilation |
| est_cost       | int  | Estimated activity costs: 0 = free or minimal costs, 1 = < $50, 2 = > $50 |
