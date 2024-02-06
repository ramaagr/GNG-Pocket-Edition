def readkml():
    f=open("./vecf-final.kml",'r')
    content=f.read().split("\n")

def find_pins(content_pins):
    pins=list() # sort of nested lists -> like [{ICAO:[PINS]}]
    
def dms_from_dd(decimal_degrees_str):
    decimal_degrees = float(decimal_degrees_str)
    degrees = int(decimal_degrees)
    remaining_minutes = (abs(decimal_degrees - degrees) * 60)
    minutes = int(remaining_minutes)
    remaining_seconds = (remaining_minutes - minutes) * 60
    seconds = int(remaining_seconds)
    fractions_of_seconds = int((remaining_seconds - seconds) * 1000)
    return degrees, minutes, seconds, fractions_of_seconds

def convert_dd_to_dms(lat,lon): # give in string formats
    lat_dat=dms_from_dd(lat)
    lon_dat=dms_from_dd(lon)

    if lat_dat[0]>=0:
        if lat_dat[0]<100:
            lat=f"N0{lat_dat[0]}.{lat_dat[1]}.{lat_dat[2]}.{lat_dat[3]}"
        else:
            lat=f"N{lat_dat[0]}.{lat_dat[1]}.{lat_dat[2]}.{lat_dat[3]}"
    else:
        if lat_dat[0]>-100:
            lat=f"S0{str(lat_dat[0])[1:]}.{lat_dat[1]}.{lat_dat[2]}.{lat_dat[3]}"
        else:
            lat=f"S{str(lat_dat[0])[1:]}.{lat_dat[1]}.{lat_dat[2]}.{lat_dat[3]}"

    if lon_dat[0]>=0:
        if lon_dat[0]<100:
            lon=f"E0{lon_dat[0]}.{lon_dat[1]}.{lon_dat[2]}.{lon_dat[3]}"
        else:
            lon=f"E{lon_dat[0]}.{lon_dat[1]}.{lon_dat[2]}.{lon_dat[3]}"
    else:
        if lon_dat[0]>-100:
            lon=f"W0{str(lon_dat[0])[1:]}.{lon_dat[1]}.{lon_dat[2]}.{lon_dat[3]}"
        else:
            lon=f"W{str(lon_dat[0])[1:]}.{lon_dat[1]}.{lon_dat[2]}.{lon_dat[3]}"
    return lat,lon
