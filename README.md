# Portfolio 2: Conditional Execution
**Course:** BES10a  
**Student:** Ethan Seth S. Gratuito

## Project Description
As a Pokemon fan and long-time battler, I have developed this program, a "Rotom Dex" Pokemon Battle Calculator that demonstrates the core concepts of conditional execution and logic flow. 

The script calculates estimated battle damage and provides tactical recommendations by utilizing:
* **Multi-way Decisions (`elif`):** To filter through different Pokemon types (Water, Fire, Grass) and output specific tactical advice based on estimated damage.
* **Nested Conditionals:** To determine type advantages (super effective vs. not very effective) by placing `if` statements inside other `if` statements.
* **Error Handling (`try / except`):** To gracefully catch `ValueError` exceptions, ensuring the program does not crash if a user inputs non-numeric characters for power or HP.
