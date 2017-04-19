### Campbell_OpenMap_Wrangling
Data wrangling project of OpenMap data of Campbell, CA, downloaded from [https://mapzen.com/]

Please read the codes and results in `P3_OpenStreetMap_CaseStudy-041717.ipynb`

### Libraries used
```
import xml.etree.ElementTree as ET
import pprint
import re
import collections
```
### Conclusion and Problems with data_sets
The OpenStreetMap data of Cambell is of a good quality but there are some typo errors as well as classification mistakes. I did not have to clean a lot of data, as most probably such cleaning was already performed in the past. Data contains lots of information about amenities but it is not clear whether it is updated regularly. This leads to the main theory behind the open map project - are there are enough diligent contributors to the map?

As we can see from sql query the top 10 contributors are pretty close to one another in contributions and it means that there is a good chance of igniting competition. It can be done via gamification. Gamification can be obtained via publicizing the competition via social networks (FB, twitter, reddit) and actually awarding certain distinctions to top contributors overall, by continent, country, state, city etc. Top contributors would be awarded certain ranks.

