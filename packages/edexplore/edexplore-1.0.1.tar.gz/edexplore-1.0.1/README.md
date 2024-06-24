# EDExplore
A simple widget for interactive EDA / QA for those who use Pandas in Jupyter Notebook.    
    
<img src="https://github.com/nagaprakashv/edexplore/assets/13671867/9ddef93e-433f-40f1-b629-886b8b00a333" width=40% height=40%>     

***
Requirements: Pandas, Jupyter Notebook, and IPyWidgets.

## How to install?
Installing IPyWidgets:     
`pip install ipywidgets`   
or      
`conda install -c conda-forge ipywidgets`   

At times, you may need to enable the ipywidgets notebook extension:    
`jupyter nbextension enable --py widgetsnbextension`

After downloading / extracting the code, go to the directory (in command line) for installation:        
`pip install .`

## How to use?
`import pandas as pd`    
`from edexplore import interact`    
`df = pd.read_csv("xzy.csv")`     
`interact(df)`    
    
<img src="https://github.com/nagaprakashv/explore/assets/13671867/7cd53826-2cf0-41f4-a335-d59bf4fd0af2"" width=100% height=100%>     
     

***
Special thanks to Ashwin Rajeev, who introduced IPyWidgets to me long back!
***
Copyright (c) 2024 Nagaprakash Venkatesan , 
[FreeBSD License](https://opensource.org/license/BSD-2-Clause)
