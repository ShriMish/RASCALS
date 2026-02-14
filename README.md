# RASCALS

**Reasoning Augmented Spacecraft Collision Avoidance Layered Simulator**

## Overview
This project deals with the simulation of a situationally-aware spacecraft digital twin, with an overlay of LLM-based reasoning to assist collision avoidance decision making for the human operator on ground. To explain this in non-jargon terms, it means I am trying to model the behaviour of a satellite which knows what is around it, or what is going to be around it, and then a machine-learning model (or the LLM in this case) helps me (or the hypothetical operator) decide whether to move my satellite to avoid a potential collision. I am doing this with the help of some very clever physics, mathematics, and systems that the misfit greats of this world have conceived for us, and my part in this simply is to be a good host and organize a grand gala, a gala of the RASCALS. Enjoy!

## Motivation
Spacecraft are beautiful machines. They are the pinnacle of engineering, and everything, I mean every profession of the world comes together to build something so unique, so fragile, yet ever so precise. They are to me only second in beauty to crewed spacecraft and landers (I know these are a subset of spacecraft!). And even then, I will not hesitate in saying we have too many of them. Too many defunct, disposed, satellites and rocket bodies in disrepair. I will add another adjective starting with "d" here. They are now deadly, or rather deadly debris. Going at an unimaginable 7.5 kilometers per second, or sometimes faster, these bodies pack a punch nothing can handle. Especially my delicate gorgeous spacecraft which are still alive. It is then imperative that we then know what is the threat, and know how to mitigate it. Before actual execution, comes planning, simulation, and testing of the knowledge we already have. Enter Digital Twins. They model systems down to the tee, and help us to understand the actual one by simulating things on its digital version. So now we build Spacecraft Digital Twins.

Next, we want this twin to check our understanding of how we avoid the debris. We can simulate collision avoidance maneuvers and strategies on it, and gain from this an understanding of how crucial it is to take the correct decision at the correct time. Yes, space is mostly a vacuum, but down here close to the Earth, there are effects that continuously alter the orbit of a spacecraft. In these very dynamic conditions (It is called flight dynamics for a reason), the probability that a collision will happen also changes with time. Therefore, early decisions can improve or worsen the chances of successful mitigation of the threat (remember the butterfly effect?). This is a very complex environment, and it will only get more complex with the number of satellites we are putting up there. Thus we need something to assist the team in making these quite subjective decisions. Enter LLMs. Large Language Models have a way of crunching the data and presenting it to us in a nuanced, readable way, which can help making these tough calls. I will be the first to say I don't understand the depth of LLMs fully (or at all!), but it is my goal to learn more through this project.

## Scope (Current)
- Early-stage development (Complete)
- Focus on environment setup and Orekit integration (Complete)
- Setting up the Spacecraft Digital Twin (In Progress)
- Include CA framework (next)

## Tech Stack
- Python
- Orekit (Python wrapper)
- VS Code
- Git/GitHub
- ChatGPT (for brainstorming and debugging assistance)

## Project Status
- Week 1: Infrastructure and repository setup
- Week 2: Setting up the Spacecraft Digital Twin and CA Framework
- Week 3:
