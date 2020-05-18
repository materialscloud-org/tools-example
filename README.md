# tools-example

This is an example tool for [materialscloud.org/tools](materialscloud.org/tools) intended 
as a starting point for developing new tools.

## Prerequisites

* [docker](https://www.docker.com/) >= v18.09
* [tools-barebone](https://github.com/materialscloud-org/tools-barebone) >= 1.0.0 

## Usage

 1. Fork the [tools-example](https://github.com/materialscloud-org/tools-example) 
 repository and rename it
    ```
    git clone https://github.com/materialscloud-org/tools-example
    mv tools-example my-tool
    ```

 2. Follow the steps explained in the README file of [tools-barebone](https://github.com/materialscloud-org/tools-barebone)
 to update _my-tool_ further.

## Build and run the example
From the main repository folder, run
```bash
./admin-tools/build-docker.sh
```
to build a docker image named `tools-example`.
Then, you can run it with
```bash
./admin-tools/run-docker.sh
```
and finally look at the result with your browser at http://localhost:8091.