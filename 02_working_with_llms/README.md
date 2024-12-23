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


## 2.4 Advanced Prompt Engineering

There are a variety of popular prompting techniques, with more being discovered every day. In the above video and below Jupyter notebook, we will walk through many of them in detail. Here, we've explained some of the bigger ones we'll be covering:

**1. Few-Shot In-Context Learning**

This approach involves feeding the model high-quality examples to steer its responses more effectively. For instance, to train a model to classify text as offensive or non-offensive, diverse examples of both categories are provided. This diversity, including failure cases, enhances the model's ability to accurately interpret and respond to similar tasks.

Example: A piece of text, "I respectfully disagree with your opinion," is presented to the model. By previously providing few-shot examples, the model is more adept at correctly classifying this as non-offensive, demonstrating the effectiveness of this method.

**2. Chain of Thought (CoT)**

The CoT technique guides the model through a series of logical steps, improving its ability to handle complex tasks that require deeper analysis. This is particularly useful for tasks that involve multiple reasoning stages.

Example: In a movie recommendation scenario, the model is instructed step-by-step to analyze various movie attributes and user requests. This structured approach allows the model to provide a well-reasoned and accurate recommendation.

**3. ReAct Framework**

ReAct combines LLMs with external tools, enhancing performance and reducing hallucinations—a common challenge with current models. This method allows the model to access and integrate external information for more accurate responses.

Example: To determine the winner of the 2023 NBA finals, React leverages a search engine to supplement the model's knowledge, demonstrating its capability to provide accurate, up-to-date information.

**4. Retrieval-Augmented Generation (RAG)**

RAG enhances prompts with contextually relevant information extracted from external databases or knowledge bases. This technique significantly improves the model's reliability by grounding its responses in specific, task-relevant data.

Example: In querying about a course, RAG utilizes text chunks and embeddings stored in vector storage to provide a detailed and accurate description of the course content.

**5. Prompt Chaining**

Prompt chaining involves breaking down a complex task into smaller subtasks, each addressed through a separate prompt. This method is particularly effective in processing and synthesizing large amounts of information.

Example: After analyzing movie recommendations, a second prompt is used to extract and present a concise user response, demonstrating the model's ability to handle detailed, multi-step processes.

Checkout the Jupyter Notebook: [1_prompt_engineering_overview_part2.ipynb](/02_working_with_llms/1_prompt_engineering_overview_part2.ipynb)

## 2.5 Logging, Tracking, and Debugging Prompts

As you scale your LLM applications, it's crucial to track and analyze prompts effectively. Comet provides a suite of tools for this purpose, including functionalities for storing results, tracking different template versions, and managing prompt chains. This capability is particularly useful when dealing with complex prompt sequences that require distinct logging approaches.

The ability to compare prompts across various models, like GPT-3.5 or GPT-4, offers valuable insights into model performance. Documenting relevant metadata, such as token usage and cost, is also a key part of this process.

In this lesson, we will be building a system that tags machine learning paper abstracts. The process begins with selecting a model and creating prompts to extract tags, which are mentions of model names. The output is a JSON object listing these tags.

This pipeline, a simplified version of a larger project, demonstrates a typical workflow for extracting and converting information and assessing output quality. The Comet tools are used to log, track, and debug prompts. Throughout the below notebook, you will get the chance to use Comet to collect and visualize your data in a way that makes it simple for you to improve your model output.

Checkout the Jupyter Notebook: [2_prompt_tracking_comet.ipynb](/02_working_with_llms/2_prompt_tracking_comet.ipynb)

## 2.6 Fine-tuning and Customizing LLMs

In this lesson, we'll explore the process of fine-tuning large language models. In our demonstration, we walk through fine-tuning an emotion classifier using a base LLM. The process involves preparing and processing the dataset, fine-tuning the model, and leveraging LLM Ops tools for tracking and iterating. Our dataset is split into training and validation sets, formatted in JSON with pairs of prompts and completions.

We use the Transformers and Datasets libraries from Hugging Face, among others, to facilitate this process. The fine-tuning involves configuring training arguments, setting hyperparameters, and executing the training process. We also discuss the importance of logging and tracking experiments for reproducibility and evaluation.

After fine-tuning, we use Comet to inspect and analyze the results. This tool provides insights into the model's performance, such as loss metrics, and allows for the exploration of different configurations and experiments. We emphasize the importance of artifacts and checkpoints for reproducibility and further analysis.

Watch the above video and follow along in the below notebook for a more detailed guide to fine-tuning, but here we've broken down the main steps from the video:

**Step 1: Select a Base Model**

The first step in fine-tuning LLMs involves choosing a suitable base model. Open-source platforms like Hugging Face's Hub offer a variety of models to start with. The choice of the base model should align with your specific requirements and interests.

**Step 2: Prepare Your Dataset**

Your fine-tuning dataset needs to be formatted appropriately. This dataset is crucial as it will directly influence the model's learning and adaptability to the task at hand.

**Step 3: Fine-Tune the Model**

Utilizing libraries like Transformers, you can fine-tune your chosen model. Fine-tuning LLMs can involve various techniques, such as reinforcement learning from human feedback, instructional tuning, and self-supervised learning. It's important to choose the most effective methods based on your specific use case.

**Step 4: Evaluate and Debug**

A critical part of the process is the evaluation and debugging of the fine-tuned model. This step ensures the model's quality and performance improvements. Remember, fine-tuning is an iterative process; hence, using tools like Comet is vital for tracking and optimizing model performance over time.

Additionally, this notebook exercise works a bit differently than others in this course in that it actually spans more than one module. The last two sections in this notebook, titled "Register Model" and "Deploy Model," will be covered later in Lesson 3. We've included them in this notebook because they depend on the model we train in this lesson, and we want to give you the option of reusing this notebook later rather than duplicating your work. For now, however, you can safely ignore them.

Checkout the Jupyter Notebook: [3_fine_tuning.ipynb](/02_working_with_llms/3_fine_tuning.ipynb)

## 2.7 Evaluating LLMs

Evaluating large language models (LLMs) like GPT-4 is a complex task. Traditional machine learning benchmarks and metrics often fall short, necessitating the creation of high-quality, bespoke evaluation datasets. This process is labor-intensive, involving thorough data cleaning and preparation.

Evaluations can be both qualitative and quantitative. While metrics such as accuracy, F1 score, semantic similarity, BLEU, and ROUGE are useful, they might not always suffice. Qualitative aspects like fluency, helpfulness, and safety are often assessed through human evaluation, which has become increasingly popular for its effectiveness in providing nuanced insights.

Given the lack of reliable automated benchmarks, human evaluation plays a crucial role in assessing the performance of models like Llama 2, GPT-4, and others. This method helps in understanding how well these models perform on specific tasks of interest.

Additionally, an emerging trend is to use LLMs themselves for evaluation. This involves setting up specific criteria or rubrics to judge the quality of model outputs for particular use cases.

In our demo project, we evaluate an emotion classifier fine-tuned on Flan-T5. The process includes:

1. **Logging our data with Comet**: We utilize Comet for logging and debugging our model. This includes importing the Comet LLM library for prompt logging and evaluation.

2. **Inspecting Model Performance**: We inspect the model's performance on actual examples and generate confusion matrices. This helps in understanding the model's proficiency in a multi-label classification task, and identifies areas of weakness for further fine-tuning. All of this is done using Comet.

3. **Comparative Analysis**: As a follow-up exercise, comparing the fine-tuned model with other models like GPT-3.5 Turbo and GPT-4 is recommended. This comparison helps in assessing the quality of both the dataset and the fine-tuning approach.

4. **Exploring Comet's Capabilities**: The final part of the demo involves going deeper into Comet to review logged results. This helps in providing a comprehensive view of the model's performance.

Effective evaluation of LLMs requires a combination of quantitative metrics, qualitative analysis, and human judgment. Tools like Comet enhance this process, enabling better insight and iterative improvement of models. As the field evolves, these tools will continue to become more sophisticated, simplifying the evaluation process.

Checkout the Jupyter Notebook: [4_evaluation.ipynb](/02_working_with_llms/4_evaluation.ipynb)