# 2. Working with LLMs

Welcome to Lesson 2!

In this lesson, we'll cover challenges and strategies for training large language models. We will also talk about how to select LLMs, how improve our model output via fine-tuning and prompt engineering, and how to track our experiments. Finally, we will cover how to evaluate LLMs.

## 2.1 Training LLMs: Strategies and Challenges

Throughout this course, we're going to discuss various challenges in working with LLMs as well as strategies for overcoming them. In particular, we're going to focus on how LLMOps can enable you to build with large language models at scale. But, before we get into LLMOps, we need to discuss some general concepts related to training LLMs.

One of the biggest decisions you'll make in an LLM-based project is whether or not you will train your own model. What you decide ultimately will shape the rest of your decisions around LLMOps. Without going too deep into the world of LLM training, here are some key considerations for deciding whether or not you will train your own LLM:

- **Training your own LLM enables customization, but increases training efforts.** By training your own model, you can get precisely the behavior you want. But, it will require extensive training, which adds significant overhead to your project.

- **LLMs require large, high-quality training data.** This isn't just about the cost of building a huge dataset, it's also about whether or not enough data exists. If you're thinking of training a model on your internal documents, for example, your library might simply be too small.

- **Computation resources are expensive at scale.** LLMs require lots of compute resources, typically GPUs, for training and inference. These come at quite a cost. It is not uncommon for companies like OpenAI or Google to report training costs in the tens of millions of dollars.

- **LLM training requires advanced tooling to operationalize.** Training an LLM can be complex, and with so many resources being committed to the process, you want to make sure you have the absolute best infrastructure in place. A wasted training run can be a huge loss.

- **Training an LLM can save on cost and latency.** Some companies train their own (typically smaller) LLMs as a cost-saving measure. If your model is able to produce the outputs you want with less prompt engineering, then it uses fewer tokens, and therefore less computation occurs. Smaller models can also be hosted more cheaply, and are generally faster.

- **Improves privacy, safety, and inference speed.** Obviously, training and hosting your own model gives you complete control over the data it accesses and the infrastructure it uses to perform inference. This puts safety and performance directly in your control.

## 2.2 Selecting your LLM

Choosing the appropriate Large Language Model (LLM) is crucial for the success of your project. The decision hinges on various factors including cost, speed, quality, model size, training data, and your specific application. In this lesson, we want to guide you through these considerations.

- **Cost**: If your primary concern is cost, you might opt for GPT 3.5 instead of the more expensive GPT-4. Fine-tuning an existing model can further reduce expenses.

- **Speed and Efficiency**: For projects where speed is a priority, consider fine-tuning your own model to optimize latency. If you want to use general-purpose model, you might use a smaller model like GPT 3.5 as opposed to GPT-4.

- **Quality Focus**: When quality is paramount, several powerful options are available. Claude and command-xlarge models are known for their exceptional output. GPT 3.5 and GPT-4 also provide good quality, but your choice may vary depending on other project-specific requirements.

- **Convenience and General Use**: Again, hosted third-party models like Claude and the GPT family are going to be the easiest to get up and running with.

- **Customization and Privacy**: If your project demands a high degree of customization or you're concerned about privacy, consider using open-source models like FLAN-T5 or Lama 2. For instance, FLAN-T5, which we will discuss in an upcoming section, is relatively easy to fine-tune for downstream tasks. However, for enhanced privacy, you might need to develop internal custom models using your own data. This approach requires more work but ensures greater control over data privacy and model behavior.

In some rare cases, using a pre-trained model may not be an option. For projects with unique requirements, pre-training your own models on large datasets might be necessary. For example, projects with specific privacy needs may require that the model only be trained on data that satisfies certain requirements, which can be impossible when using third-party models.

Selecting the right model for your project depends on various factors like cost, speed, quality, and specific use cases. Remember, the models mentioned here are just a few examples of the plethora available. There are numerous domain-specific models and open-source options, each with different licensing terms. You should make use of resources like [Hugging Face's Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard), which ranks open source LLMs according to different benchmarks, when selecting your model.


## 2.3 Basics of Prompt Engineering

Prompt engineering is a major focus in a lot of LLM research today, and for good reason. It is one of the most effective ways to improve the quality of LLM outputs. Doing it well can be the difference between a reliable and unreliable model.

The bulk of the information in this lesson is contained in the Jupyter notebook, below, which we will walk through together in the above video. Below, we've extracted some of our advice from the video for developing good prompts:

- **Specificity and Clarity**: Avoid ambiguous instructions. Be explicit in your prompts to ensure precise and relevant outputs.

- **Using Delimiters**: Delimiters (e.g. `###`) help structure and clarify prompts, especially when dealing with multiple information sections.

- **Specify Output Format**: Explicitly state the desired format of the output, whether it's free text, markdown, HTML, or a structured format like JSON.

- **Prompt Chaining**: Breaking down a task into subtasks (prompt chaining) can significantly improve the quality and accuracy of the outputs.

- **Think Step-by-Step**: Instructing the model to reason step-by-step through a problem can enhance the performance, especially in tasks involving complex reasoning.

- **Role-Playing**: Implementing role-playing in prompts, where the model assumes a specific role like a research assistant, can improve the quality and relevance of responses.

Checkout the Jupyter Notebook: [1_prompt_engineering_overview_part1.ipynb](/02_working_with_llms/1_prompt_engineering_overview_part1.ipynb)