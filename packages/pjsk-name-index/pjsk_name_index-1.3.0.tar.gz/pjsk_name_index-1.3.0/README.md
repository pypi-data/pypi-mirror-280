# pjsk-name-index
> A library for indexing names from the game Project Sekai. (Python achieve)

# Index
## sekai_index() method
### Field Name Table
| Field       | Field Meaning                          |
| ------------ |---------------------------------------|
| full_name    | Team English Name/Role English Name    |
| full_name_cn | Team Chinese Name/Role Chinese Name    |
| simple_name  | Team Abbreviation/Role Abbreviation   |
| joke_name_cn | (For roles only) Role Nickname (Alias) |
| full_name_cn_official | (For teams only) Team Official Chinese Name |
The `pjsk-name-index` library provides the `sekai_index()` method, which can quickly index to other names of the corresponding role based on the provided parameters.
### Usage:
`sekai_index('Full Role Name/Full Team Name','Team Type (team or individual)').expected field`
### Example:
``` Python
from pjsk_name_index import sekai_index
print(sekai_index("knd","individual")['full_name_cn'])
// Output Result: > 宵崎奏
print(sekai_index("狮雨星绊","team")['full_name'])
// Output Result: > Leo/need
```
# License
MIT License