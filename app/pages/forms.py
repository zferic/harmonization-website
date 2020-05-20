from django import forms

""" (Name that will be send on the http request, name of the feature) """

PLOT_TYPES = (
    ("scatter_plot", "scatter_plot"),
    ("pair_plot", "pair_plot"),
    ("cat_plot", "cat_plot"),
    ("violin_cat_plot", "violin_cat_plot")
)

DPI_CHOICES = (
    (100, "low_res"),
    (300, "high_res")
)

FEATURE_CHOICES = (
    ("sepal_length", "sepal_length"),
    ("sepal_width", "sepal_width"),
    ("petal_length", "petal_length"),
    ("petal_width", "petal_width"),
    ("flower_type", "flower_type"),
)
)


class FlowersForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(FlowersForm, self).__init__(*args, **kwargs)
        self.initial['plot_type'] = PLOT_TYPES[0][0]
        self.initial['x_feature'] = FEATURE_CHOICES[0][0]
        self.initial['y_feature'] = FEATURE_CHOICES[1][0]
        self.initial['color_by'] = FEATURE_CHOICES[4][0]
        self.initial['fig_dpi'] = DPI_CHOICES[0][0]
        self.initial['plot_name'] = 'New Plot'

    plot_name = forms.CharField(max_length=100,
                                help_text="Type the name of your next plot.")
    plot_type = forms.ChoiceField(choices=PLOT_TYPES)
    x_feature = forms.ChoiceField(choices=FEATURE_CHOICES)
    y_feature = forms.ChoiceField(choices=FEATURE_CHOICES)
    color_by = forms.ChoiceField(choices=FEATURE_CHOICES)
    fig_dpi = forms.ChoiceField(choices=DPI_CHOICES,
                                help_text="low_res=100dpi, high_res=300dpi.")
