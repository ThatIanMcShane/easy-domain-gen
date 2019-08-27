#! usr/bin/env python3

# examples.py // easyDomainGen.py
# some example usage 
import easyDomainGen

print('---')
print('Example Usage')
print('---')
# Get one domain
print(easyDomainGen.getRandomDomain())
print('--')
# Get the full list of domains
fullList = easyDomainGen.getAllDomains()
print(str(len(fullList)))
print('--')

# Get specific number of domains
smallList = easyDomainGen.getMultipleRandomDomains(5)
print(str(len(smallList)) + ' domains returned')
for x in smallList:
    print(x)

