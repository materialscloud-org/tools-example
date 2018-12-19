# tools-example

This is an example tool for [materialscloud.org/tools](materialscloud.org/tools) intended as a starting point for developing new tools.

## Prerequisites

* [docker](https://www.docker.com/) >= v18.09
* [tools-barebone]((https://github.com/materialscloud-org/tools-example) docker image installed (see instructions there)

## Usage

 1. Fork the [tools-example](https://github.com/materialscloud-org/tools-example) repository and rename it
    ```
    git clone https://github.com/materialscloud-org/tools-example
    mv tools-example my-tool  # also rename on github!
    cd my-tool
    ./build-docker.sh   # build the tools-example docker image
    ```
 1. Run the example app:
    * `./run-docker.sh` and open open http://localhost:8091 to check the web interface
    * `./enter-docker.sh` to get a shell on the container

 1. Start editing the example to fit your needs

   * `config.yml`
   * `user_templates` folder
   * ...
