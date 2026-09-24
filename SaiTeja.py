import streamlit as st
# Page configuration
st.set_page_config(
    page_title="Thermodynamics Calculator",
    page_icon="🌡️",
    layout="centered"
)

st.title("🌡️ Thermodynamics Calculator")
st.write("Select a calculation from the sidebar.")


# Work done during expansion
def work_done(pressure, initial_volume, final_volume):
    return pressure * (final_volume - initial_volume)


# Heat supplied
def heat_supplied(mass, specific_heat, initial_temperature, final_temperature):
    return mass * specific_heat * (final_temperature - initial_temperature)


# Change in internal energy
def change_internal_energy(heat, work):
    # First Law of Thermodynamics:
    # ΔU = Q - W
    return heat - work


# Heat engine efficiency
def heat_engine_efficiency(heat_supplied_value, heat_rejected):
    work_output = heat_supplied_value - heat_rejected
    efficiency = (work_output / heat_supplied_value) * 100
    return work_output, efficiency


# Sidebar menu
st.sidebar.header("Select Calculation")

choice = st.sidebar.selectbox(
    "Choose an option:",
    [
        "Work Done During Expansion",
        "Heat Supplied",
        "Change in Internal Energy",
        "Efficiency of Heat Engine"
    ]
)


# 1. Work Done
if choice == "Work Done During Expansion":

    st.header("🔧 Work Done During Expansion")

    pressure = st.number_input(
        "Pressure (Pa)",
        min_value=0.0,
        value=100000.0
    )

    initial_volume = st.number_input(
        "Initial Volume (m³)",
        min_value=0.0,
        value=1.0
    )

    final_volume = st.number_input(
        "Final Volume (m³)",
        min_value=0.0,
        value=2.0
    )

    if st.button("Calculate Work"):
        work = work_done(
            pressure,
            initial_volume,
            final_volume
        )

        st.success(f"Work done = {work:.2f} J")


# 2. Heat Supplied
elif choice == "Heat Supplied":

    st.header("🔥 Heat Supplied")

    mass = st.number_input(
        "Mass (kg)",
        min_value=0.0,
        value=1.0
    )

    specific_heat = st.number_input(
        "Specific Heat Capacity (J/kg-K)",
        min_value=0.0,
        value=4186.0
    )

    initial_temperature = st.number_input(
        "Initial Temperature (K)",
        min_value=0.0,
        value=300.0
    )

    final_temperature = st.number_input(
        "Final Temperature (K)",
        min_value=0.0,
        value=400.0
    )

    if st.button("Calculate Heat"):
        heat = heat_supplied(
            mass,
            specific_heat,
            initial_temperature,
            final_temperature
        )

        st.success(f"Heat supplied = {heat:.2f} J")


# 3. Change in Internal Energy
elif choice == "Change in Internal Energy":

    st.header("⚡ Change in Internal Energy")

    heat = st.number_input(
        "Heat supplied to the system (J)",
        value=1000.0
    )

    work = st.number_input(
        "Work done by the system (J)",
        value=400.0
    )

    if st.button("Calculate Internal Energy"):

        delta_u = change_internal_energy(
            heat,
            work
        )

        st.success(f"Change in internal energy = {delta_u:.2f} J")

        st.info("Formula: ΔU = Q - W")


# 4. Heat Engine Efficiency
elif choice == "Efficiency of Heat Engine":

    st.header("⚙️ Efficiency of Heat Engine")

    heat_supplied_value = st.number_input(
        "Heat supplied to the engine (J)",
        min_value=0.01,
        value=1000.0
    )

    heat_rejected = st.number_input(
        "Heat rejected by the engine (J)",
        min_value=0.0,
        value=400.0
    )

    if st.button("Calculate Efficiency"):

        work_output, efficiency = heat_engine_efficiency(
            heat_supplied_value,
            heat_rejected
        )

        st.success(f"Work output = {work_output:.2f} J")
        st.success(f"Efficiency = {efficiency:.2f}%")

        st.info("Formula: η = (Work Output / Heat Supplied) × 100")


# Footer
st.sidebar.markdown("---")
st.sidebar.write("Thermodynamics Calculator")
st.sidebar.write("Built with Streamlit")
