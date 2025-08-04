class Incident:
    def __init__(self, type, lat, lng, magnitude, location, time, source, id=None):
        self.id = id  # optional: not used in DB insert
        self.type = type
        self.lat = float(lat) if lat not in [None, ""] else None
        self.lng = float(lng) if lng not in [None, ""] else None
        self.magnitude = float(magnitude) if magnitude not in [None, ""] else None
        self.location = location
        self.time = time
        self.source = source

def safe_float(val):
    try:
        return float(val)
    except:
        return None


