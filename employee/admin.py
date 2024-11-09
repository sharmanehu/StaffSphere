from django.contrib import admin
from .models import EmployeeDetail, EmployeeExperience, EmployeeEducation
import matplotlib.pyplot as plt
import pandas as pd
import io
import base64
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class EmployeeAdmin(admin.ModelAdmin):
    change_list_template = "admin/employee_changelist.html"

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)
        if response.context_data:
            self.create_chart()
            self.perform_logistic_regression()
            best_employee = self.get_best_employee()
            response.context_data['chart'] = self.chart_data
            response.context_data['accuracy'] = self.accuracy
            response.context_data['best_employee'] = best_employee
        return response

    def create_chart(self):
        employees = EmployeeExperience.objects.all().values('company1duration', 'company2duration', 'company3duration')
        df = pd.DataFrame(employees)
        experience_counts = df.count()

        plt.figure(figsize=(10, 5))
        plt.bar(experience_counts.index, experience_counts.values, color='skyblue')
        plt.xlabel('Experience Categories')
        plt.ylabel('Number of Employees')
        plt.title('Employee Distribution by Work Experience')
        plt.xticks(rotation=45)
        plt.grid(axis='y')

        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        self.chart_data = base64.b64encode(buf.read()).decode('utf-8')
        plt.close()


#Algorithm.......
    def perform_logistic_regression(self):
        employees = EmployeeExperience.objects.all().values('company1duration', 'company2duration', 'company3duration', 'target')
        df = pd.DataFrame(employees)

        X = df[['company1duration', 'company2duration', 'company3duration']]
        y = df['target']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = LogisticRegression()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        self.accuracy = accuracy_score(y_test, y_pred)

    def get_best_employee(self):
        employees = EmployeeExperience.objects.all()
        best_employee = None
        highest_experience = 0

        for employee in employees:
            total_experience = employee.company1duration + employee.company2duration + employee.company3duration
            if total_experience > highest_experience:
                highest_experience = total_experience
                best_employee = employee

        return best_employee

admin.site.register(EmployeeDetail, EmployeeAdmin)
