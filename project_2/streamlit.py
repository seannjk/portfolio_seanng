import numpy as np
import pandas as pd
import pickle
 

st.set_page_config(
    page_icon='📖',
    initial_sidebar_state='expanded'
)

st.title("ProPrata's Application")

st.write('Use the sidebar to select a page to view.')

page = st.sidebar.selectbox(
    'Page',
    ('Home', 'Form')
)

# @st.cache
# def load_data():
#     df = pd.read_csv('data/austen_poe.csv')
#     return df

if page == 'Home':
    st.subheader('Home Page')
    st.write("Hello, welcome to ProPrata's Application")

if page == 'Form':
    # header
    st.subheader('Home Qualities')
    st.write('''Input the qualities of your desired home.''')

    # get user input
    neigh_qual = st.number_input('neighborhood_by_medianprice', format='%d', min_value=int(0), value=int(0))
    overall_qual = st.number_input('overall_home_quality', format='%d', min_value=int(0), step=1, value=int(0))
    local_feature = st.number_input('positive_features', format='%d', min_value=int(0), value=int(0))
    outside = st.number_input('outdoor_porch_space', format='%d', min_value=int(0), step=100, value=int(0))
    shop = st.number_input('garage_space', format='%d', min_value=int(0), step=100, value=int(0))
    cars_garage = st.number_input('size_of_car_garage', format='%d', min_value=int(0), step=1, value=int(0))
    age = st.number_input('building_age', format='%d', min_value=int(0), step=1, value=int(0))
    room_size = st.number_input('size_of_rooms', format='%d', min_value=int(0), step=1, value=int(0))
    basement_qual = st.number_input('basement_quality', format='%d', min_value=int(0), step=1, value=int(0))
    basement_ceiling = st.number_input('basement_ceiling_height', format='%d', min_value=int(0), step=1, value=int(0))
    bsmt = st.number_input('finished_basement_in_sqft', format='%d', min_value=int(0), step=100, value=int(0))
    kitchen = st.number_input('kitchen_quality', format='%d', min_value=int(0), step=1, value=int(0))
    fire = st.number_input('fireplace_quality', format='%d', min_value=int(0), step=1, value=int(0))
    upstairs = st.number_input('finished_upstairs_in_sqft', format='%d', min_value=int(0), step=1, value=int(0))
    rooms = st.number_input('rooms_upstairs', format='%d', min_value=int(0), step=1, value=int(0))
    remodel = st.number_input('remodeled_home', format='%d', min_value=int(0), step=1, value=int(0))
    single_story = st.number_input('single_storey_home', format='%d', min_value=int(0), step=1, value=int(0))
    multi_story = st.number_input('multiple_storey_home', format='%d', min_value=int(0), step=1, value=int(0))
    middle_townhouse = st.number_input('middle_unit_townhouse', format='%d', min_value=int(0), step=1, value=int(0))
    end_townhouse = st.number_input('end_unit_townhouse', format='%d', min_value=int(0), step=1, value=int(0))
    fam_house = st.number_input('family_house', format='%d', min_value=int(0), step=1, value=int(0))
    exter_qual = st.number_input('quality_of_exterior_material', format='%d', min_value=int(0), step=1, value=int(0))
    type_exter = st.number_input('type_of_exterior_covering_house', format='%d', min_value=int(0), step=1, value=int(0))
    roof_qual = st.number_input('good_roof_quality', format='%d', min_value=int(0), step=1, value=int(0))
    vaneer_sqft = st.number_input('masonry_veneer_sqft', format='%d', min_value=int(0), step=100, value=int(0))
    bldg_func = st.number_input('home_functionality', format='%d', min_value=int(0), step=1, value=int(0))
    lot_front = st.number_input('lot_frontage', format='%d', min_value=int(0), step=10, value=int(0))
    lot_size = st.number_input('lot_size', format='%d', min_value=int(0), step=100, value=int(0))
    paved = st.number_input('paved_driveway', format='%d', min_value=int(0), step=1, value=int(0))
    heater_qual = st.number_input('heater_quality', format='%d', min_value=int(0), step=1, value=int(0))
    total_baths = st.number_input('total_number_of_baths', format='%d', min_value=int(0), step=1, value=int(0))



    data = np.array([neigh_qual, overall_qual, local_feature, outside, shop,cars_garage, age,room_size,
    basement_qual, basement_ceiling, bsmt, kitchen,fire, upstairs, rooms, remodel, single_story, multi_story, middle_townhouse, end_townhouse,
    fam_house, exter_qual, type_exter, roof_qual, vaneer_sqft, bldg_func, lot_front, lot_size, paved, heater_qual,total_baths]).reshape(1, -1)

    st.subheader('Make a prediction')

    with open('./finalized_model.sav', 'rb') as pickle_in:
        model = pickle.load(pickle_in)

    predicted_price = model.predict(data)[0]
    

    st.subheader('Results:')
    st.write(f'Your home is worth {round(predicted_price, 2)}. Go you!')
