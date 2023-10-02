# Session 18 : 27/9/2023

## What is SQL trigger ?

An SQL trigger allows you to specify SQL actions that should be executed automatically when a specific event occurs in the database.

```sql
CREATE TRIGGER log_user_data
AFTER INSERT ON users
FOR EACH ROW
BEGIN
    INSERT INTO user_creation_log(id, created_at, created_by)
    VALUES (NEW.id, NOW(), NEW.created_by)
END;
```

## Libraries for 3d modeling

- Numpy-stl
- PyMesh
- PyTorch3d
- SolidPython
- PyVista

## Graphs that is supported by seaborn and not supported by matplotlib with examples

- Scatterplot Matrix

```python
import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")
sns.pairplot(iris, hue="species")
plt.show()
```

- Categorical Plots

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
sns.barplot(x="day", y="total_bill", data=tips)
plt.show()
```

- Distribution Plots

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.distplot(tips["total_bill"])
plt.show()
```

- Heatmaps

```python
import seaborn as sns
import matplotlib.pyplot as plt

corr_matrix = tips.corr()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.show()
```

- Facet Grids

```python
import seaborn as sns
import matplotlib.pyplot as plt

g = sns.FacetGrid(tips, col="time", row="smoker")
g.map(sns.scatterplot, "total_bill", "tip")
plt.show()
```
## Make a Dashboard with smartvis