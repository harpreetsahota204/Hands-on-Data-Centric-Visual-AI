| Module 1: Course Introduction |
|-------------------------------|

| Stage 1 – Desired Results |
|---------------------------|

| ESTABLISHED GOALS |
|-------------------|
| - Understand and articulate the difference between model-centric and data-centric AI approaches, and recognize the importance of data quality in AI model development. |
| - Differentiate between object detection and semantic segmentation tasks, and determine when to use each approach based on specific use cases and requirements. |
| - Explain the evaluation process for object detection and semantic segmentation models, including the commonly used metrics and their significance in assessing model performance. |
| - Interpret and analyze the values of evaluation metrics for object detection and semantic segmentation models, and use these insights to make informed decisions about model selection and improvement. |
| - Develop proficiency in using FiftyOne to load datasets, fine-tune/apply models, and evaluate model performance, enabling hands-on experience with data-centric AI workflows. |

| Transfer |
|----------|
| Students will be able to independently use their learning to… |
| - Analyze real-world problem scenarios and determine whether object detection or semantic segmentation is the most appropriate task based on the specific requirements and constraints of the use case. |
| - Select the most suitable model architecture for the chosen task, considering factors such as performance, computational efficiency, and dataset characteristics. |
| - Identify and justify the most appropriate evaluation metrics for assessing the performance of the selected model, based on the specific goals and requirements of the use case. |
| - Preprocess and load datasets into the FiftyOne format |
| - Apply the selected model to the loaded dataset using FiftyOne, fine-tuning the model parameters as necessary to optimize performance for the specific use case. |
| - Evaluate the performance of the applied model using the selected evaluation metrics, interpreting the results and drawing insights to guide further model improvement and decision-making. |

| Meaning |
|---------|

| UNDERSTANDINGS |
|---------------|
| Students will understand that… |
| - Data quality plays a crucial role in determining the performance and reliability of AI models, with high-quality data leading to better model outcomes and low-quality data resulting in suboptimal or biased results. |
| - Establishing a baseline model is essential for evaluating the effectiveness of subsequent model improvements and data enhancements, providing a reference point for measuring progress and guiding iterative refinements. |
| - Model-centric AI focuses primarily on improving model architectures and algorithms, while data-centric AI emphasizes the importance of data quality, labeling, and curation in driving model performance and generalization. |
| - The iterative process of improving both data and model in tandem is key to the success of data-centric AI, involving a continuous cycle of analyzing model performance, identifying data quality issues, enhancing the dataset, retraining the model, and evaluating the results. |

| ESSENTIAL QUESTIONS |
|--------------------|
| - Why should I place more emphasis on debugging my datasets than debugging my model architecture? |
| - How can we quantify and assess the quality of a dataset, and what are the key factors to consider when evaluating dataset suitability for a specific AI task? |
| - How does the iterative process of data-centric AI differ from the traditional model-centric approach, and what are the benefits and challenges of adopting a data-centric mindset? |
| - What role do evaluation metrics play in guiding data-centric AI improvements, and how can we select appropriate metrics that align with the specific goals and requirements of a given use case? |
| - How can tools like FiftyOne streamline and enhance the data-centric AI workflow, and what are the key features and capabilities that make them valuable for data management, model evaluation, and visual exploration? |

| Acquisition |
|------------|

| Students will know… |
|--------------------|
| Students will know the principles, approaches, and best practices of data-centric AI for object detection and semantic segmentation, including dataset quality, evaluation metrics, and tools like FiftyOne. |

| Students will be skilled at… |
|-----------------------------|
| - Preprocessing and transforming raw data into formats suitable for object detection and semantic segmentation tasks, ensuring compatibility with FiftyOne and other data-centric AI tools. |
| - Loading and managing datasets using FiftyOne, leveraging its capabilities for data visualization, annotation, and quality assessment to gain insights into dataset characteristics and potential issues. |
| - Exploring and analyzing datasets using FiftyOne's interactive interface, identifying patterns, biases, and areas for improvement in data quality and representation. |
| - Selecting appropriate models from the FiftyOne model zoo or other sources based on task requirements, dataset characteristics, and performance considerations, demonstrating an understanding of model architectures and trade-offs. |
| - Applying selected models to datasets using FiftyOne, configuring model parameters, and fine-tuning as needed to optimize performance for specific use cases. |
| - Evaluating model performance using relevant metrics provided by FiftyOne, interpreting evaluation results, and deriving insights to guide iterative model and dataset improvements. |
| - Identifying and addressing data quality issues revealed through model evaluation, such as labeling errors, data imbalance, or biases, and implementing strategies for dataset refinement and enhancement. |

| Stage 2 – Evidence and Assessment |
|-----------------------------------|

| Evaluative Criteria |
|--------------------|
| - Accuracy, as measured by number of correct questions on quiz |
| - Technical proficiency, as measured the ability to arrive at a correct solution for a coding exercise |

| Assessment Evidence |
|--------------------|

| PERFORMANCE TASK(S): |
|---------------------|
| Implementing code using the FiftyOne SDK |

| OTHER EVIDENCE: |
|----------------|
| A 15 question quiz consisting of: |
| - 10 conceptual questions |
| - 5 questions which will require the learner to write code to arrive at the correct answer. Examples include: loading a dataset into FiftyOne format, apply a model from the model zoo to the dataset, report various performance metrics, answer general questions about the dataset |

| Stage 3 – Learning Plan |
|-------------------------|

| Summary of Key Learning Events and Instruction |
|-----------------------------------------------|
| 1. **Lesson 1 - Introduction to Data-Centric AI:** Discuss the limitations of model centric thinking, the importance of data quality for building models, the consequences of models trained on bad data, discuss the model centric v data centric AI paradigms, talk about high profile shifts to data centric AI thinking in the industry, and share examples data centric AI methodologies. I'll also provide links to additional reading material. |
| 2. **Lesson 2 - Understanding the Data and Model Feedback Loop:** Discuss the iterative process of improving both the data and the model in tandem, that is analyze model performance, identify data quality issues, enhance dataset based on insights, retrain model with improved data, repeat process for continuous optimization |
| 3. **Lesson 3 - The Role of Datasets and Benchmarks in Computer Vision:** I'll discuss the critical role of high-quality datasets and benchmarks in developing, evaluating, and comparing computer vision models, including dataset characteristics, labeling formats, and popular examples like LVIS. |
| 4. **Lesson 4 - Object Detection (define the Tasks and discuss how to select Models):** A crash course on tasks of object detection, the model architectures commonly used for this tasks, considerations for selecting a model architecture, what models we will use, and an brief overview of what transfer learning is. |
| 5. **Lesson 5 - Evaluation Metrics for Object Detection:** Discuss common metrics for evaluating object detection|
| 6. **Lesson 6 - Getting Started with FiftyOne:** Common data formats for object detection, how to load datasets into FiftyOne, and a brief overview of FiftyOne (compare and contrast to pandas). I'll also provide links to FiftyOne documentation, cookbooks, and the model and dataset zoo where students can learn more. |
| 7. **Lesson 7 - Hands-on: Evaluating Baseline Model Performance with FiftyOne:** In this lesson I will walk students through code to show them how to apply a model to a dataset in FiftyOne and evaluate that models performance |