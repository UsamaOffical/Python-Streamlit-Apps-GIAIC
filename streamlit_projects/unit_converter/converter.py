import streamlit as st

st.set_page_config(page_title="Unit Converter", layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #192436;
    }
    .main-title {
        font-size: 50px;
        font-weight: bold;
        text-align: center;
        color: #04B6D2;
        margin-bottom: 0px;
    }
    .sub-title {
        font-size: 28px;
        text-align: center;
        color: #E0E0E0;
    }
    .stButton>button {
        margin-top: 24px;
        background-color: #04B6D2;
        color: white;
        padding: 12px 28px;
        font-size: 18px;
        font-weight: bold;
        border-radius: 8px;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease-in-out;
    }
    .stButton>button:hover {
        background-color: #0396A6;
        color:rgb(231, 224, 224);
        transform: scale(1.05);
    }
    .custom-success {
        background-color: #F1E3D3;
        color: black;
        font-size: 18px;
        font-weight:600;
        padding: 8px;
        border-radius: 6px;
        text-align: center;
        margin-top: 20px;
    }
    .sidebar-title {
        font-size: 22px;
        font-weight: bold;
        color: #4A90E2;
        margin-bottom: 10px;
    }
    .sidebar-history {
        background-color: #2F3949;
        color: white;
        padding: 10px;
        font-size: 16px;
        font-weight: bold;
        border-radius: 8px;
        margin-bottom: 5px;
        text-align: center;
        border-left: 5px solid #04B6D2;
    }
    [data-testid="stSidebar"] {
        background-color: #2F3949;
        border-right: 1px solid #4A90E2;
    }
    div[data-testid="stSelectbox"] label,
    div[data-testid="stNumberInput"] label {
        color: white;
        font-size: 18px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown('<div class="sidebar-title">Conversion History</div>', unsafe_allow_html=True)
if "history" not in st.session_state:
    st.session_state.history = []

if st.sidebar.button("Clear History"):
    st.session_state.history = []

st.markdown('<div class="main-title">Unit Converter</div>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Smart, Simple, and Hassle-Free Unit Conversion.</p>', unsafe_allow_html=True)

# Define conversion factors
conversion_factors = {
    "Length": {
        "meter": {
            "meter": 1,
            "centimeter": 100,
            "millimeter": 1000,
            "kilometer": 0.001,
            "inch": 39.3701,
            "foot": 3.28084,
            "yard": 1.09361,
            "mile": 0.000621371
        },
        "centimeter": {
            "meter": 0.01,
            "centimeter": 1,
            "millimeter": 10,
            "kilometer": 0.00001,
            "inch": 0.393701,
            "foot": 0.0328084,
            "yard": 0.0109361,
            "mile": 0.00000621371
        },
        "millimeter": {
            "meter": 0.001,
            "centimeter": 0.1,
            "millimeter": 1,
            "kilometer": 0.000001,
            "inch": 0.0393701,
            "foot": 0.00328084,
            "yard": 0.00109361,
            "mile": 6.21371e-7
        },
        "kilometer": {
            "meter": 1000,
            "centimeter": 100000,
            "millimeter": 1000000,
            "kilometer": 1,
            "inch": 39370.1,
            "foot": 3280.84,
            "yard": 1093.61,
            "mile": 0.621371
        },
        "inch": {
            "meter": 0.0254,
            "centimeter": 2.54,
            "millimeter": 25.4,
            "kilometer": 0.0000254,
            "inch": 1,
            "foot": 0.0833333,
            "yard": 0.0277778,
            "mile": 0.0000157828
        },
        "foot": {
            "meter": 0.3048,
            "centimeter": 30.48,
            "millimeter": 304.8,
            "kilometer": 0.0003048,
            "inch": 12,
            "foot": 1,
            "yard": 0.333333,
            "mile": 0.000189394
        },
        "yard": {
            "meter": 0.9144,
            "centimeter": 91.44,
            "millimeter": 914.4,
            "kilometer": 0.0009144,
            "inch": 36,
            "foot": 3,
            "yard": 1,
            "mile": 0.000568182
        },
        "mile": {
            "meter": 1609.34,
            "centimeter": 160934,
            "millimeter": 1609340,
            "kilometer": 1.60934,
            "inch": 63360,
            "foot": 5280,
            "yard": 1760,
            "mile": 1
        }
    },
    "Mass": {
        "kilogram": {
            "kilogram": 1,
            "gram": 1000,
            "milligram": 1000000,
            "pound": 2.20462,
            "ounce": 35.274
        },
        "gram": {
            "kilogram": 0.001,
            "gram": 1,
            "milligram": 1000,
            "pound": 0.00220462,
            "ounce": 0.035274
        },
        "milligram": {
            "kilogram": 0.000001,
            "gram": 0.001,
            "milligram": 1,
            "pound": 0.00000220462,
            "ounce": 0.000035274
        },
        "pound": {
            "kilogram": 0.453592,
            "gram": 453.592,
            "milligram": 453592,
            "pound": 1,
            "ounce": 16
        },
        "ounce": {
            "kilogram": 0.0283495,
            "gram": 28.3495,
            "milligram": 28349.5,
            "pound": 0.0625,
            "ounce": 1
        }
    },
    "Time": {
        "second": {
            "second": 1,
            "minute": 1/60,
            "hour": 1/3600,
            "day": 1/86400
        },
        "minute": {
            "second": 60,
            "minute": 1,
            "hour": 1/60,
            "day": 1/1440
        },
        "hour": {
            "second": 3600,
            "minute": 60,
            "hour": 1,
            "day": 1/24
        },
        "day": {
            "second": 86400,
            "minute": 1440,
            "hour": 24,
            "day": 1
        }
    }
}

categories = {
    "Length": ["meter", "centimeter", "millimeter", "kilometer", "inch", "foot", "yard", "mile"],
    "Mass": ["kilogram", "gram", "milligram", "pound", "ounce"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Time": ["second", "minute", "hour", "day"]
}

category = st.selectbox("Category", list(categories.keys()))
value = st.number_input("Enter Value", min_value=0.0, format="%.2f")
col1, col2, col3 = st.columns([1, 0.2, 1])

from_unit = col1.selectbox("From", categories[category], key="from_unit")
to_unit = col3.selectbox("To", categories[category], key="to_unit")

def swap_units():
    st.session_state.to_unit, st.session_state.from_unit = st.session_state.from_unit, st.session_state.to_unit

col2.button("⇄", on_click=swap_units, key="swap")

if st.button("Convert", key="convert_button"):
    try:
        if category == "Temperature":
            if from_unit == "celsius" and to_unit == "fahrenheit":
                result = (value * 9/5) + 32
            elif from_unit == "fahrenheit" and to_unit == "celsius":
                result = (value - 32) * 5/9
            elif from_unit == "celsius" and to_unit == "kelvin":
                result = value + 273.15
            elif from_unit == "kelvin" and to_unit == "celsius":
                result = value - 273.15
            elif from_unit == "fahrenheit" and to_unit == "kelvin":
                result = (value - 32) * 5/9 + 273.15
            elif from_unit == "kelvin" and to_unit == "fahrenheit":
                result = (value - 273.15) * 9/5 + 32
            else:
                result = value
        else:
            # Use the conversion factors
            result = value * conversion_factors[category][from_unit][to_unit]
        
        result_text = f"{value} {from_unit} = {result:.2f} {to_unit}"
        
        st.markdown(
            f"""
            <div class="custom-success">
                {result_text}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.session_state.history.append(result_text)

    except Exception as e:
        st.error(f"Invalid conversion: {str(e)}")

if st.session_state.history:
    st.sidebar.markdown("### Past Conversions:")
    for entry in st.session_state.history[-5:]:
        st.sidebar.markdown(f'<div class="sidebar-history">{entry}</div>', unsafe_allow_html=True)