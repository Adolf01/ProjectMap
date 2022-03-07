import folium
m = folium.Map(location=[22.5554,72.9945],zoom_start=11,tiles="Stamenterrain")

folium.TileLayer('OpenStreetMap',attr='OpenStreetMap').add_to(m)
folium.TileLayer('https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png',name='Stadia.AlidadeSmoothDark'
,attr='Stadia.AlidadeSmoothDark').add_to(m)


folium.LayerControl().add_to(m)



folium.Marker([22.539648321623243, 72.89364390874803],popup="krishna Hospital",tooltip="cases:1500 bed-avai:700 occupied:800", icon=folium.Icon(icon="medkit",prefix="fa",color="red")).add_to(m)
folium.Marker([22.555532005277357, 72.9310501316682],popup="Panchayat Hospital",tooltip="cases:1100 bed-avai:800 occupied:210", icon=folium.Icon(icon="medkit",prefix="fa",color="red")).add_to(m)
folium.Marker([22.560793099913568, 72.92376726118222],popup="Aradhana Hospital",tooltip="cases:1000 bed-avai:700 occupied:300", icon=folium.Icon(icon="medkit",prefix="fa",color="red")).add_to(m)
folium.Marker([22.561046371510894, 72.92275887072397],popup="Prerana Hospital",tooltip="cases:150 bed-avai:100 occupied:50", icon=folium.Icon(icon="medkit",prefix="fa",color="red")).add_to(m)
folium.Marker([22.566748278832637, 72.94584967616869],popup="Zydus Hospital",tooltip="cases:200 bed-avai:100 occupied:100", icon=folium.Icon(icon="medkit",prefix="fa",color="red")).add_to(m)
folium.Marker([22.56453598165028, 72.94522552380218],popup="Iris Hospital",tooltip="cases:400 bed-avai:250 occupied:150", icon=folium.Icon(icon="medkit",prefix="fa",color="red")).add_to(m)
folium.Marker([22.562115692581266, 72.94842756309392],popup="Shreeji Psychratic Hospital",tooltip="cases:1500 bed-avai:700 occupied:800", icon=folium.Icon(icon="medkit",prefix="fa",color="red")).add_to(m)
folium.Marker([22.562235885871807, 72.94880454238415],popup="Shashwat Hospital",tooltip="cases:350 bed-avai:200 occupied:150", icon=folium.Icon(icon="medkit",prefix="fa",color="red")).add_to(m)
folium.Marker([22.56321125437212, 72.96027846501002],popup="Jamna Hospital",tooltip="cases:450 bed-avai:300 occupied:150", icon=folium.Icon(icon="medkit",prefix="fa",color="red")).add_to(m)
folium.Marker([22.56021291093387, 72.96112960604894],popup="Meera Hospital",tooltip="cases:400 bed-avai:300 occupied:100", icon=folium.Icon(icon="medkit",prefix="fa",color="red")).add_to(m)
folium.Marker([22.564965942342628, 72.94872380289787],popup="Himalya Hospital",tooltip="cases:250 bed-avai:100 occupied:150", icon=folium.Icon(icon="medkit",prefix="fa",color="red")).add_to(m)
folium.Marker([22.56559178312618, 72.95011929868618],popup="Kusum Children Hospital",tooltip="cases:100 bed-avai:80 occupied:20", icon=folium.Icon(icon="medkit",prefix="fa",color="red")).add_to(m)
folium.Marker([22.565589925480214, 72.95040696560142],popup="Tsquare Hospital",tooltip="cases:900 bed-avai:700 occupied:200", icon=folium.Icon(icon="medkit",prefix="fa",color="red")).add_to(m)
folium.Marker([22.55655146914618, 72.95876536448482],popup="Maa Hospital",tooltip="cases:850 bed-avai:600 occupied:250", icon=folium.Icon(icon="medkit",prefix="fa",color="red")).add_to(m)
folium.Marker([22.55691300525526, 72.95743030910604],popup="Astha Hospital ",tooltip="cases:750 bed-avai:500 occupied:200", icon=folium.Icon(icon="medkit",prefix="fa",color="red")).add_to(m)
folium.Marker([22.5573743665248, 72.95738795607535],popup="Chaitanya Hospital",tooltip="cases:700 bed-avai:400 occupied:300", icon=folium.Icon(icon="medkit",prefix="fa",color="red")).add_to(m)
folium.Marker([22.558392663813276, 72.9576246000592],popup="Shreeji Women Hospital",tooltip="cases:800 bed-avai:500 occupied:300", icon=folium.Icon(icon="medkit",prefix="fa",color="red")).add_to(m)
folium.Marker([22.558921175515923, 72.95821408643907],popup="Deep Hospital",tooltip="cases:550 bed-avai:300 occupied:250", icon=folium.Icon(icon="medkit",prefix="fa",color="red")).add_to(m)
folium.Marker([22.559306560703114, 72.96114925620266],popup="Satyam Hospital",tooltip="cases:600 bed-avai:400 occupied:200", icon=folium.Icon(icon="medkit",prefix="fa",color="red")).add_to(m)
folium.Marker([22.56130194258607, 72.96039895330304],popup="Rutu General Hospital",tooltip="cases:500 bed-avai:300 occupied:200", icon=folium.Icon(icon="medkit",prefix="fa",color="red")).add_to(m)
folium.Marker([22.56167187904674, 72.96369752857409],popup="Apollo Hospital",tooltip="cases:1200 bed-avai:400 occupied:800", icon=folium.Icon(icon="medkit",prefix="fa",color="red")).add_to(m)


m.save('map.html')




