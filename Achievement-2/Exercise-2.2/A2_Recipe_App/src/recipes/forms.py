from django import forms

# Form to search recipes and select chart type
class RecipeSearchForm(forms.Form):
    recipe_title = forms.CharField(max_length=100, required=False, label="Recipe Title")
    chart_type = forms.ChoiceField(
        choices=[('Bar', 'Bar chart'), ('Pie', 'Pie chart'), ('Line', 'Line chart')],
        required=False,
        label="Chart Type"
    )
