
I downloaded the Arabic Generated Abstracts dataset from the Hugging Face Datasets library.

The dataset contains three splits

1. by_polishing(generated from human-written abstracts) -> 2851 rows
2. from_title(generated from paper titles only) ->2963 -rows
3. from_title_and_content(generated using both title and paper content)->2574 rows

- Each split has the same five features.

1. original_abstract(The original human-written Arabic abstract)
2. allam_generated_abstract(Machine-generated  using the Allam model)
3. jais_generated_abstract(Machine-generated  using the Jais model)
4. llama_generated_abstract(Machine-generated t using the LLaMA model)
5. openai_generated_abstract(Machine-generated t using the OpenAI model)


- Data Types:

- All features are object (text/string) data 
- All features are 100% complate with no missing values

task 1.2
result : 

DatasetDict({
    by_polishing: Dataset({
        features: ['original_abstract', 'allam_generated_abstract', 'jais_generated_abstract', 'llama_generated_abstract', 'openai_generated_abstract'],
        num_rows: 2851
    })
    from_title: Dataset({
        features: ['original_abstract', 'allam_generated_abstract', 'jais_generated_abstract', 'llama_generated_abstract', 'openai_generated_abstract'],
        num_rows: 2963
    })
    from_title_and_content: Dataset({
        features: ['original_abstract', 'allam_generated_abstract', 'jais_generated_abstract', 'llama_generated_abstract', 'openai_generated_abstract'],
        num_rows: 2574
    })
})