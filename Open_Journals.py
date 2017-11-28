
# coding: utf-8

# In[1]:

articles = "OneDrive/Andrew Academy/PLOS/Open_Psychol_J/PMC4636039.nxml"


# In[2]:

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


# In[3]:

tree = ET.parse(articles)
tree.getroot()


# In[ ]:

root = tree.getroot()
root


# In[ ]:

root.tag, root.attrib


# In[ ]:

for child in root:
    print child.tag, child.attrib


# In[ ]:

root[0].tag


# In[ ]:

for elem in tree.iter():
    print elem.tag, elem.text


# In[ ]:

for elem in tree.iter(tag='title'):
    print elem.text
    


# In[ ]:

for child in root:
    for grandchild in child:
        print grandchild


# In[ ]:

for elem in tre

tree.findall('front')
# In[ ]:

all_things = tree.findall('front')
all_things


# In[ ]:

all_things[1].attrib


# In[ ]:



