import streamlit as st
import pandas as pd
import joblib

# 配置 Streamlit 页面
st.set_page_config(
    page_title="Pt-Leaching&Pd-Leaching&Rh-Leaching Prediction",
    page_icon="🔬"
)
 
# 直接显示欢迎信息（无需登录）
st.write('Welcome metal leaching prediction!')


   
xgb_Pt = joblib.load('xgb_Pt.pkl')
xgb_Pd = joblib.load('xgb_Pd.pkl')
rf_Rh = joblib.load('rf_Rh.pkl')
   
st.title('Pt-Leaching&Pd-Leaching&Rh-Leaching Prediction')
    
    
    
dict1 = {
    'X19': {
        "Li2CO3": 74,
        "Na2CO3": 106,
        "NaCl": 58.5
    },
    'X22': {
        "Air": 0,
        "H2": 1,
        "O2": 2,
        "CO": 3,
        "Cl2": 4
    },
    'X24': {
        "HCl": -8
    },
    'X26': {
        "H2SO4": -2,
        "HNO3": -1.8,
        "Malic acid": 1.92,
        "Citric acid": 3.13,  # 注意这里修正了拼写错误 "Ctric" -> "Citric"
        "Formic acid": 3.75,
        "Acetic acid": 4.76
    },
    'X29': {
        "NaClO3": 106,
        "CuCl2": 134,
        "NaCl": 58.5,
        "AlCl3": 133.5,
        "FeCl3·6H2O": 270.5,  # 注意这里的化学式可能需要特定的格式或转义字符，但这里假设它是有效的字符串
        "CuCl2·2H2O": 171,
        "CaCl2": 111,
        "NaClO": 74.5
    }
} 
              
   

X1 = st.sidebar.slider(label = 'Particle size ', min_value = 20.0,
                              max_value = 2830.0 ,
                              value = 500.0,
                              step = 10.0)
                               
X2 = st.sidebar.slider(label = 'Pd in feed ', min_value = 0.0,
                              max_value = 0.54 ,
                              value = 0.20,
                              step = 0.01)    
X3 = st.sidebar.slider(label = 'Pt in feed', min_value = 0.0057,
                              max_value =0.4154 ,
                              value = 0.28,
                              step = 0.0001) 
X4 = st.sidebar.slider(label = 'Rh in feed', min_value = 0.00512,
                              max_value = 0.03 ,
                              value = 0.014,
                              step = 0.0001)
X5 = st.sidebar.slider(label = 'Al in feed', min_value = 2.0,
                              max_value = 42.0 ,
                              value = 35.83,
                              step = 0.5) 
X6 = st.sidebar.slider(label = 'Si in feed', min_value = 1.8,
                              max_value = 21.0 ,
                              value = 19.27,
                              step = 1.0) 
X7 = st.sidebar.slider(label = 'Mg in feed', min_value = 0.6,
                              max_value = 11.34 ,
                              value = 10.92,
                              step = 0.1) 
X8 = st.sidebar.slider(label = 'La in Feed', min_value = 0.009,
                              max_value = 3.2,
                              value = 0.52,
                              step = 0.1) 
X9 = st.sidebar.slider(label = 'Nd in feed', min_value = 0.0,
                              max_value = 1.1,
                              value = 0.75,
                              step = 0.1)                         
X10 = st.sidebar.slider(label = 'Ce in feed', min_value = 0.13,
                              max_value = 19.0,
                              value = 3.06,
                              step = 0.1)                         
X11 = st.sidebar.slider(label = 'Fe in feed', min_value = 0.2371,
                              max_value = 2.408,
                              value = 1.45,
                              step = 0.1)                          
X12 = st.sidebar.slider(label = 'Ca in feed', min_value = 0.069,
                              max_value = 1.0,
                              value = 0.88,
                              step = 0.01)                          
X13 = st.sidebar.slider(label = 'Zn in feed', min_value = 0.019,
                              max_value = 0.56,
                              value = 0.0,
                              step = 0.01)                          
X14 = st.sidebar.slider(label = 'Zr in feed', min_value = 0.08,
                              max_value = 16.5,
                              value = 5.41,
                              step = 0.1)                         
X15 = st.sidebar.slider(label = 'Na in feed', min_value = 0.148,
                              max_value = 1.0,
                              value = 0.0,
                              step = 0.1) 
X16 = st.sidebar.slider(label = 'Mn in feed', min_value = 0.0164,
                              max_value = 1.18,
                              value = 0.91,
                              step = 0.01)
X17 = st.sidebar.slider(label = 'Ti in feed', min_value = 0.22,
                              max_value = 0.402,
                              value = 0.22,
                              step = 0.1)
X18 = st.sidebar.slider(label = 'Pb in feed', min_value = 0.069,
                              max_value = 7.66,
                              value = 0.00,
                              step = 0.01)
                             
X19 = st.sidebar.selectbox('Roasting additive type', ["Li2CO3",
"Na2CO3",
"NaCl",
]) 
    
    
X20 = st.sidebar.slider(label = 'Mass ratio to waste', min_value = 0.0,
                              max_value = 100.0 ,
                              value = 0.0,
                              step = 0.1)
    
X21 = st.sidebar.slider(label = 'Roasting temperature ', min_value = 0.0,
                              max_value = 950.0 ,
                              value = 800.0,
                              step = 10.0)
                              
X22 = st.sidebar.selectbox('Atmosphere', ["Air",
"H2",
"O2",
"CO",  
"Cl2",
 ]) 

X23 = st.sidebar.slider(label = 'Roasting time ', min_value = 0.0,
                              max_value = 1320.0 ,
                              value = 120.0,
                              step = 10.0)
X24 = st.sidebar.selectbox('1-acid',["HCl",
 ]) 

 
    
X25 = st.sidebar.slider(label = '1-Acid Conc ', min_value = 0.0,
                              max_value = 13.0 ,
                              value = 10.0,
                              step = 0.1)     
                              
X26 = st.sidebar.selectbox('2-acid',["H2SO4",
"H3P04",
"HNO3",
"Malic acid",
"Ctric acid",
"Formic acid",
"Acetic acid",
])    
  
X27 = st.sidebar.slider(label = '2-Acid Conc ', min_value = 0.0,
                              max_value = 11.0,
                              value = 1.6,
                              step = 0.1)   
                              
X28 = st.sidebar.slider(label = 'H2O2', min_value = 0.0,
                              max_value = 10.0 ,
                              value = 5.0,
                              step = 0.1)   

                              
X29 = st.sidebar.selectbox('Leaching additive typle',["NaClO3",
"CuCl2",
"NaCl",
"AlCl3",
"FeCl3·6H2O"
"CuCl2·2H2O"
"CaCl2"
"NaClO"
])    
X30 = st.sidebar.slider(label = 'Leaching additive amount', min_value = 0.0,
                              max_value = 10.0 ,
                              value = 5.0,
                              step = 0.1)    
X31 = st.sidebar.slider(label = 'Leaching time', min_value = 5.0,
                              max_value = 600.0 ,
                              value = 150.0,
                              step = 1.0)    
X32 = st.sidebar.slider(label = 'Leaching temperature', min_value = 20.0,
                              max_value = 180.0 ,
                              value = 95.0,
                              step = 1.0)    
X33 = st.sidebar.slider(label = 'Pulp density', min_value = 0.1,
                              max_value = 800.0 ,
                              value = 150.0,
                              step = 0.1)    
X34 = st.sidebar.slider(label = 'Speed', min_value = 0.0,
                              max_value = 600.0 ,
                              value = 150.0,
                              step = 1.0)    
        
features = {'Particle size ':X1, 'Pd in feed ':X2, 'Pt in feed':X3, 'Rh in feed':X4, 'Al in feed':X5,
       'Si in feed':X6, 'Mg in feed':X7, 'La in feed':X8, 'Nd in feed':X9, 'Ce in feed':X10, 'Fe in feed':X11, 'Ca in feed':X12, 'Zn in feed':X13, 'Zr in feed':X14, 'Na in feed':X15, 
       'Mn in feed':X16, 'Ti in feed':X17, 'Pb in feed':X18, 'Roasting additive type':dict1['X19'][X19], 
       'Mass ratio to waste':X20, 'Roasting temperature ':X21, 'Atmosphere':dict1['X22'][X22], 'Roasting time ':X23,'1-acid':dict1['X24'][X24], '1-Acid Conc ':X25,
       '2-acid':dict1['X26'][X26], '2-Acid Conc ':X27, 'H2O2':X28, 'Leaching additive typle':dict1['X29'][X29],'Leaching additive amount':X30,
        'Leaching time':X31, 'Leaching temperature':X32, 'Pulp density':X33, 'Speed':X34,
      }
features_df  = pd.DataFrame([features])
st.dataframe(
    features_df,
    use_container_width=True,  # 自动适应容器宽度
    height=100  # 可选：固定高度触发垂直滚动
)  

if st.button('Predict'):
        prediction = xgb_Pt.predict(features_df)
        a=prediction[0]
        if a<0:
            a=0
        if a>100:
            a=100
        st.write(' Pt-Leaching: '+ str(a))
        prediction = xgb_Pd.predict(features_df)
        a=prediction[0]
        if a<0:
            a=0
        if a>100:
            a=100
        st.write(' Pd-Leaching: '+ str(a))
        prediction = rf_Rh.predict(features_df)
        a=prediction[0]
        if a<0:
            a=0
        if a>100:
            a=100
        st.write(' Rh-Leaching: '+ str(a))                  
