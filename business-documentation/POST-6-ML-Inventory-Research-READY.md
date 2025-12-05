Our colleagues at Windesheim just published something worth reading. A systematic review of machine learning in inventory control, analyzing 122 studies from 1980 to 2024.

Here's what jumped out: most companies are still using ML to forecast demand, then plugging those forecasts into old optimization models. Separate steps. But that's changing.

The paper shows three ways ML gets used in inventory management:

**Forecast first, optimize later.** This is the safe approach. Use ML for demand forecasting, feed it into your existing systems. Easy to explain to stakeholders. But forecast accuracy doesn't always translate to better inventory decisions.

**Integrate ML into optimization.** Skip the forecasting step entirely. Train the model directly on inventory costs (overage vs. underage). Works well for single-period problems like newsvendor setups. Still pretty new territory for most companies.

**Reinforcement learning.** Let an AI agent learn by trial and error in a simulated environment. This one's getting attention because it can handle messy real-world problems: multiple locations, uncertain lead times, perishable products. The catch? It's computationally expensive and hard to explain.

What's missing from most of this research? Real-world data. Out of 51 reinforcement learning papers, only a handful used actual company data. Most tested on simulations.

And here's a gap that matters for supply chain sustainability: almost nobody is studying product obsolescence. Electronics don't rot, but they become worthless fast. Where's the ML research on that?

At Value Chain Hackers, we're interested in the transparency angle. How do you prove your "AI-optimized inventory" actually works? How do you trace decisions back through black-box models when auditors or sustainability reports ask?

The full paper breaks down what inventory problems have been tackled (spoiler: mostly simple ones) and which ones are still wide open. Worth a read if you're thinking about where ML actually fits in supply chain operations versus where it just sounds impressive.

Published in Operations Research Perspectives, open access: https://doi.org/10.1016/j.orp.2025.100367

Have you tried ML for inventory decisions in your organization? What actually worked versus what stayed in the pilot phase?

#MachineLearning #InventoryManagement #SupplyChain #AI #ReinforcementLearning #ValueChainHackers #SupplyChainTransparency #OperationsResearch #DataScience #SupplyChainOptimization
