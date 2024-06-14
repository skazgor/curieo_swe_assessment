# curieo_swe_assessment

## Requirements
- python 3.8

## Run the code
Clone the code and open the terminal in the root directory of the project. 

### Task 1
```bash
python task1.py <input_file>
```
### Task 2
```bash
python task2.py <input_file>
```

## Test file generation
```bash
python input_generator.py <output_file> <Initial_balance> <Number_of_transactions> <Number_of_queries> <1/2(to indicate which task formats)>
```

## Run and build the docker image
```bash
docker build -t curieo_swe_assessment
docker run -it curieo_swe_assessment
```