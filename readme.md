# Battling Pokémon Teams (PokéLab)

Our app utilizes the Python-Implemented **PokéAPI** to assemble teams of 6 Pokémon and perform fundamental analysis based on the team’s type composition. We are also using a **MongoDB** database to collect and store every single team made using our service (as long as you provide an identifier/name).

Using a dropdown menu, any of the teams stored in the database can be called upon for a battle (coded in **Javascript**). You can either play with two people or have one of the teams controlled by a bot. During the battle sequence, you have the option of launching one of two attacks, using a potion, or swapping the Pokémon in play. Type effectiveness is also fully implemented using a large array that compares types.

This moveset is not representative of the official games, but effectively, every Pokemon can still choose from 4 different moves during a turn.

![1](https://user-images.githubusercontent.com/47545637/115163087-c5c70a00-a06c-11eb-9390-6653e6c4eb78.png)
![2](https://user-images.githubusercontent.com/47545637/115163089-c790cd80-a06c-11eb-80e6-5b48fe81e3c3.png)
![3](https://user-images.githubusercontent.com/47545637/115163090-c8c1fa80-a06c-11eb-90d8-fb9273d15a23.png)
