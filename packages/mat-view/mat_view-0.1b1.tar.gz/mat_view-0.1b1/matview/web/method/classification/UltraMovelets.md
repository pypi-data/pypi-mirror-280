### UltraMovelets (and RandomMovelets)

\[ [publication](https://#) \] \[ [GitHub](https://github.com/ttportela/MoveletsDiscovery) \] \[ [JAR](https://github.com/ttportela/MoveletsDiscovery/releases/download/v1.2.0/MoveletDiscovery.jar) \]


**UltraMovelets: Efficient Movelet Extraction for Multiple Aspect Trajectory Classification**, published in The 35th International Conference on Database and Expert Systems Applications (DEXA 2024)
 

## Versions


This is a project of the thesis: *Towards Optimization Methods for Movelets Extraction in Multiple Aspect Trajectory Classification (Portela, 2023)*, provided also these two methods:


- *RandomMovelets*: randomly evaluates subtrajectories to discover movelets (`-version random`). 
- *UltraMovelets*: uses a recursive incremental strategy to limit the search space (`-version ultra`). Most memory efficient method.

\* *RandomMovelets* uses Log limit for trajectory size by default, use `-Ms -1` to disable Log limit if is set by default.

## Setup

A. In order to run the code you first need to install Java 8 (or superior). Be sure to have enough RAM memory available. 

B. Download the `MoveletDiscovery.jar` file from the releases, or compile and export the jar file for the main class: `br.ufsc.mov3lets.run.Mov3letsRun`

## Usage

### 1. You can run the HIPERMovelets with the following command:

```Shell
-curpath "$BASIC_PATH" 
-respath "$RESULT_PATH" 
-descfile "$DESC_FILE"  
-version ultra
-nt 8
```


Where:
- `BASIC_PATH`: The path for the input CSV training and test files.
- `RESULT_PATH`: The destination folder for CSV results files.
- `DESC_FILE`: Path for the descriptor file. File that describes the dataset attributes and similarity measures.
- `-version`: Method to run (ultra, random, hiper, hiper-pivots, ...)
- `-nt`: Number of threads

    
### 2. For instance:

To run the UltraMovelets you can run the java code with the following default entries as example:


```Shell
java -Xmx80G -jar MoveletDiscovery.jar 
-curpath "$BASIC_PATH" -respath "$RESULT_PATH" -descfile "$DESC_FILE" 
-version ultra -nt 8 -ed true -samples 1 -sampleSize 0.5 -medium "none" -output "discrete" -lowm "false" -ms 1 -Ms -3 | tee -a "output.txt"
```


This will run with 80G memory limit, 8 threads, and save the output to the file `output.txt`.

It is the same as (without the output file):

```Shell
java -Xmx80G -jar MoveletDiscovery.jar 
-curpath "$BASIC_PATH" -respath "$RESULT_PATH" -descfile "$DESC_FILE" 
-version ultra -nt 8
```

### Examples

**UltraMovelets**


```Shell
java -jar MoveletDiscovery.jar 
-curpath "$BASIC_PATH" -respath "$RESULT_PATH" -descfile "$DESC_FILE" 
-version ultra 
```

**RandomMovelets**


```Shell
java -jar MoveletDiscovery.jar 
-curpath "$BASIC_PATH" -respath "$RESULT_PATH" -descfile "$DESC_FILE" 
-version random
```

**To a complete list of parameters:**

```Shell
java -jar MoveletDiscovery.jar --help
```

## Change Log

Refer to [CHANGELOG.md](./CHANGELOG.md).

## Author

Tarlis Portela

<!--##### Reference:

| Title | Authors | Year | Venue | Links | Cite |
|:------|:--------|------|:------|:------|:----:|
| UltraMovelets: Efficient Movelet Extraction for Multiple Aspect Trajectory Classification | Portela, T. T.; Machado, V. L.; Carvalho, J. T.; Bogorny, V.; Bernasconi, A.: Renso, C. | 2024 | The 35th International Conference on Database and Expert Systems Applications (DEXA 2024) | [Article](https://doi.org/#) [Repository](https://github.com/ttportela/MoveletsDiscovery) | [BibTex](https://github.com/github.com/ttportela/MoveletsDiscovery/blob/master/bibliography.bib) |
-->