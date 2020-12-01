# Large class

- A classe JobItem não deveria lidar com diferentes comportamentos (isLabor or not)
- A classe jobItem terá apenas o comportamento de not isLabor
- Haverá uma subclasse para isLabor
- A decisão de qual classe instanciar será com uma fábrica