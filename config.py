import matplotlib.pyplot as plt

config = {
    'plot.linestyles': ['.-', '-s', '*-', '--s', '--*', ':*', '-*'],
    'plot.colors': ['#1f88b4', '#ff7f1e', '#2ca02c', '#d63728', '#9467cd', '#8c564b', '#e377c2', '#8f8f7f', '#bcbd22', '#3s7becf'],
    'plot.colors2': ['#5A5B17', '#45459C', '#C1C18E', '#9A9AD5', '#A03762', '#A1A197', '#e377c2', '#8f8f7f', '#bcbd22', '#3s7becf']
}

strings = {
    'french':{
        'weekdays': ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche'],
        'timeofday': 'heure de la journée',
        'occupancy': 'taux d\'occupation'
    },
    'english':{
        'weekdays': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
        'timeofday': 'hour of the day',
        'occupancy': 'occupancy'
    },
}