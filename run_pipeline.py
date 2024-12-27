from src.pipeline import Pipeline

pipeline_file = "valid_pipeline.yaml"
# Remove comment to test failures
# pipeline_file = "invalid_pipeline_module.yaml"  # Non-existing module
# pipeline_file = "invalid_pipeline_ordering.yaml" # Invalid module order
# pipeline_file = "invalid_pipeline_params.yaml" # Invalid module params

pipeline = Pipeline(pipeline_file)

input_text = "This is a sample input text."

result = pipeline.run(input_text)
print("Pipeline result:", result)
