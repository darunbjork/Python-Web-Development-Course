from django import forms

# Form to search recipes and select chart type
class RecipeSearchForm(forms.Form):
    recipe_title = forms.CharField(max_length=100, required=False, label="Recipe Title")
    cooking_time = forms.IntegerField(required=False, label="Cooking Time (minutes)")  # Numeric field for cooking time
    difficulty = forms.ChoiceField(
        choices=[('', 'Select Difficulty'), ('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')],
        required=False,
        label="Difficulty"
    )
    category = forms.CharField(max_length=100, required=False, label="Category")
    chart_type = forms.ChoiceField(
        choices=[('Bar', 'Bar chart'), ('Pie', 'Pie chart'), ('Line', 'Line chart')],
        required=False,
        label="Chart Type"
    )
