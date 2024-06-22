# Plugin Testing Framework for eWaterCycle

[//]: # (## Badges)
[//]: # (TODO: On some READMEs, you may see small images that convey metadata, such as whether or not all the tests are passing for the project. You can use Shields to add some to your README. Many services also have instructions for adding a badge.)

## Description
The projects goal is to develop a comprehensive and extendable testing framework for hydrological model plugins that intend to integrate with the eWaterCycle platform. This framework will ensure the accuracy and reliability of these models, such that they can be used and compared, properly and consistently inside the eWaterCycle platform.

## Installation
Install the conda environment as specified by the eWaterCycle documentation [here](https://ewatercycle.readthedocs.io/en/latest/system_setup.html#conda-environment). 

Then just run:
```
pip install ewatercycle-model-testing
```
Inside your terminal.

## Usage
To see examples and explanations of how to use and extend the testing framework, please read the WIKI or documentation.

## Contributing
Any additions to the repository should follow the code style guidelines as specified here:

- **pytest** passes, with >90% code coverage for the added code.
- **pylinting** gives 10/10 following the rules specified in the pyproject.toml file, which should be located automatically.
- **pydocstyle** gives no issues (every method and class is accompanied by a correctly formatted docstring)

## Authors and acknowledgment
This project is developed by 
- Konrad Gniaź
- Ferdi Helvensteijn
- Robert Mertens
- Alexander van den Arend Schmidt
- Floris van der Voorn

We extend our gratitude to our client Rolf Hut for the opportunity to work on this project, and to Timur Oberhuber (Teaching Assistant), Burcu Ozkan (TU Coach), and Martin Skrodzki (TU Coordinator) for their guidance.

## License
This project is licensed under the Apache License 2.0 - see the LICENSE file for details. This is the same license as is used by eWaterCycle [here](https://github.com/eWaterCycle/ewatercycle/blob/main/LICENSE).

## Project status
This project is ongoing up until the final presentation as scheduled on the 27th of June.
