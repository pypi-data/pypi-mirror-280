### HiPerMovelets

\[ [publication](https://doi.org/10.1080/13658816.2021.2018593) \] \[ [GitHub](https://github.com/ttportela/MoveletsDiscovery) \] \[ [JAR](https://github.com/ttportela/MoveletsDiscovery/releases/download/v1.2.0/MoveletDiscovery.jar) \]


**HiPerMovelets: high-performance movelet extraction for trajectory classification**, published in International Journal of Geographical Information Science
 

## Versions


This is a project with the HIPERMovelets (Portela, 2020) implementation, with three options of optimizations.


- *HiPerMovelets*: new optimization for MASTERMovelets, with greedy search (`-version hiper`).
- *HiPerPivots*: limits the movelets search space to the points that are neighbour of well qualified movelets of size one (`-version hiper-pivots`).

\* Uses Log limit for trajectory size by default, use `-Ms -1` to disable Log limit if is set by default.

## Setup

A. In order to run the code you first need to install Java 8 (or superior). Be sure to have enough RAM memory available. 

B. Download the `MoveletDiscovery.jar` file from the releases, or compile and export the jar file for the main class: `br.ufsc.mov3lets.run.Mov3letsRun`

## Usage

### 1. You can run the HIPERMovelets with the following command:

```Shell
-curpath "$BASIC_PATH" 
-respath "$RESULT_PATH" 
-descfile "$DESC_FILE"  
-version hiper
-nt 8
```


Where:
- `BASIC_PATH`: The path for the input CSV training and test files.
- `RESULT_PATH`: The destination folder for CSV results files.
- `DESC_FILE`: Path for the descriptor file. File that describes the dataset attributes and similarity measures.
- `-version`: Method to run (hiper, hiper-pvt, ...)
- `-nt`: Number of threads

    
### 2. For instance:

To run the HIPERMovelets you can run the java code with the following default entries as example:


```Shell
java -Xmx80G -jar MoveletDiscovery.jar 
-curpath "$BASIC_PATH" -respath "$RESULT_PATH" -descfile "$DESC_FILE" 
-version hiper -nt 8 -ed true -samples 1 -sampleSize 0.5 -medium "none" -output "discrete" -lowm "false" -ms 1 -Ms -3 | tee -a "output.txt"
```


This will run with 80G memory limit, 8 threads, and save the output to the file `output.txt`.

It is the same as (without the output file):

```Shell
java -Xmx80G -jar MoveletDiscovery.jar 
-curpath "$BASIC_PATH" -respath "$RESULT_PATH" -descfile "$DESC_FILE" 
-version hiper -nt 8
```

### Examples

**HIPERMovelets** (with log)


```Shell
java -jar MoveletDiscovery.jar 
-curpath "$BASIC_PATH" -respath "$RESULT_PATH" -descfile "$DESC_FILE" 
-version hiper 
```

**HIPERMovelets-Pivots** (with log)


```Shell
java -jar MoveletDiscovery.jar 
-curpath "$BASIC_PATH" -respath "$RESULT_PATH" -descfile "$DESC_FILE" 
-version hiper-pivots 
```

**To a complete list of parameters:**

```Shell
java -jar MoveletDiscovery.jar --help
```

## Change Log

Refer to [CHANGELOG.md](./CHANGELOG.md).

## Author

Tarlis Portela

##### Reference:

| Title | Authors | Year | Venue | Links | Cite |
|:------|:--------|------|:------|:------|:----:|
| HiPerMovelets: high-performance movelet extraction for trajectory classification | Portela, T. T.; Carvalho, J. T.; Bogorny, V. | 2022 | International Journal of Geographical Information Science | [Article](https://doi.org/10.1080/13658816.2021.2018593) [Repository](https://github.com/bigdata-ufsc/HiPerMovelets) | [BibTex](https://github.com/bigdata-ufsc/research-summary/blob/master/resources/bibtex/Portela2020hipermovelets.bib) |