# Axie Gene Parser for Python

### WIP - haven't ported all the stuff the other module has (Mostly because I only find the genes useful)

This is a port of the Javascript version of a plugin, you can find it here: [agp-npm](https://github.com/ShaneMaglangit/agp-npm)

It parses the Axie Infinity hexadecimal gene strings into a human-readable format.

## Install

You can use pip to install:

```python
pip install agp-py
```

## Usage

First you need to get an Axie Gene String (You can use [Axie Infinity GraphQL](https://axie-graphql.web.app/)), after that you can start:

We will be using `0x30000000032cb3300c2320c80c2308c20c63184c04c1304c0c6331420c8320c8` as our hex string.

```python
from agp_py import AxieGene

hex_string = '0x30000000032cb3300c2320c80c2308c20c63184c04c1304c0c6331420c8320c8'
hex_type = 256
gene = AxieGene(hex_string, hex_type)
print(gene.genes)
```

The `AxieGene` class requires 2 arguments, First one is the hex string, Second one is the hex type (Either 256 or 512)

Then you can access the genes by using the method `genes`, it will give you a dictionary with the gene data.

```python
{
    'cls': 'plant', 
    'region': 'global', 
    'tag': '', 
    'bodySkin': '', 
    'pattern': {'d': '000011', 'r1': '001011', 'r2': '001011'}, 
    'color': {'d': 'efd636', 'r1': 'efd636', 'r2': 'ffffff'}, 
    'eyes': {
        'd': {'class': 'plant', 'name': 'Papi', 'partId': 'eyes-papi', 'specialGenes': '', 'type': 'eyes'}, 
        'r1': {'class': 'plant', 'name': 'Cucumber Slice', 'partId': 'eyes-cucumber-slice', 'specialGenes': '', 'type': 'eyes'}, 
        'r2': {'class': 'plant', 'name': 'Cucumber Slice', 'partId': 'eyes-cucumber-slice', 'specialGenes': '', 'type': 'eyes'},
        'mystic': False
    }, 
    
    # Other parts ....
}
```