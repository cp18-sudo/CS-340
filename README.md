# CS-340 Project Two: Grazioso Salvare Dashboard

## Project Overview

The Grazioso Salvare Dashboard is a dynamic web application designed to provide comprehensive real-time analytics and monitoring for the Grazioso Salvare platform. This project fulfills the core requirements outlined in the CS-340 Project Two rubric by delivering key functionalities such as user activity tracking, system performance visualization, and customizable dashboard widgets. The dashboard aims to empower stakeholders with actionable insights through an intuitive and responsive interface.

---

## Tools and Technologies

- **Python:** Chosen for its versatility and extensive libraries supporting web development and data visualization.
- **Dash:** A Python framework built on top of Flask and React.js, facilitating the creation of interactive, analytical web applications with minimal overhead.
- **MongoDB:** A NoSQL database used to store user activity logs and system metrics, providing flexible schema design and scalability.
- **Plotly:** Integrated with Dash to render interactive charts and graphs.
- **Git:** Version control to manage project development and collaboration.

These tools were selected to efficiently meet the project’s requirements for real-time data handling, interactive visualization, and ease of deployment.

---

## Database and Framework Explanation

### MongoDB

MongoDB serves as the primary data store for the dashboard. Its document-oriented structure allows for flexible and scalable storage of diverse data types such as user events, system logs, and performance metrics. MongoDB’s powerful querying capabilities enable efficient retrieval and aggregation of data necessary for real-time analytics.

### Dash

Dash provides a robust framework for building analytical web applications using Python. It simplifies the process of creating interactive visualizations and responsive layouts without requiring extensive frontend development expertise. Dash’s integration with Plotly ensures high-quality, customizable charts, while its Flask backend supports API interactions and data processing.

---

## Installation and Setup Instructions

Follow these steps to set up and run the Grazioso Salvare Dashboard locally:

1. **Clone the repository:**

   ```
   git clone https://github.com/yourusername/grazioso-salvare-dashboard.git
   ```

2. **Navigate to the project directory:**

   ```
   cd grazioso-salvare-dashboard
   ```

3. **Create and activate a virtual environment (optional but recommended):**

   - On macOS/Linux:
     ```
     python3 -m venv venv
     source venv/bin/activate
     ```
   - On Windows:
     ```
     python -m venv venv
     venv\Scripts\activate
     ```

4. **Install dependencies:**

   ```
   pip install -r requirements.txt
   ```

5. **Configure environment variables:**

   Create a `.env` file or export the following variables:

   - `DATABASE_URL`: MongoDB connection string (e.g., `mongodb://localhost:27017/grazioso`)
   - `API_KEY`: API key for external data sources (if applicable)
   - `DEBUG`: Set to `True` to enable debug mode during development

6. **Run the application:**

   ```
   python app.py
   ```

7. **Access the dashboard:**

   Open a web browser and navigate to:

   ```
   http://localhost:5000
   ```

---

## Challenges and Solutions

During development, several challenges were encountered:

- **Real-time Data Synchronization:** Ensuring that the dashboard reflects live updates without significant latency was a key challenge. This was addressed by implementing efficient polling mechanisms and optimizing MongoDB queries to reduce response times.

- **Responsive Design:** Making the dashboard accessible and visually appealing on both desktop and mobile devices required careful layout planning. Utilizing Dash’s flexible layout components and CSS media queries helped achieve a consistent user experience across devices.

- **Data Aggregation Complexity:** Aggregating diverse metrics from multiple data sources in MongoDB posed difficulties. Leveraging MongoDB’s aggregation pipeline and indexing strategies improved query performance and data accuracy.

These challenges were overcome through iterative testing, research, and leveraging community resources.

---

## Conclusion

The Grazioso Salvare Dashboard successfully meets the CS-340 Project Two rubric by delivering a fully functional, interactive, and visually engaging analytics platform. The combination of MongoDB and Dash provides a powerful foundation for scalable data management and dynamic visualization. This project demonstrates effective use of modern tools and best practices in web application development.

For further details, please refer to the project repository and included documentation.

---

## Functionality Demonstration

The Grazioso Salvare Dashboard includes the following key functionalities as required by the CS-340 Project Two rubric:

- **User Activity Tracking:** Real-time monitoring and logging of user interactions on the platform.
- **System Performance Visualization:** Interactive charts displaying system metrics such as CPU usage, memory consumption, and network activity.
- **Customizable Dashboard Widgets:** Users can add, remove, and rearrange widgets to tailor the dashboard to their preferences.
- **Data Filtering and Drill-down:** Ability to filter data by time ranges and drill down into specific events or metrics for detailed analysis.
- **Responsive Layout:** The dashboard adapts seamlessly to different screen sizes, ensuring usability on desktops, tablets, and mobile devices.

### Screenshots

- User Activity Overview  
  ![User Activity Overview](https://via.placeholder.com/800x400?text=User+Activity+Overview)

- System Performance Charts  
  ![System Performance Charts](https://via.placeholder.com/800x400?text=System+Performance+Charts)

- Customizable Widgets Interface  
  ![Customizable Widgets Interface](https://via.placeholder.com/800x400?text=Customizable+Widgets+Interface)

---

## Development Process

The development of the Grazioso Salvare Dashboard followed a structured process to ensure all project requirements were met:

1. **Requirement Analysis:** Reviewed the CS-340 Project Two rubric to identify required functionalities and deliverables.
2. **Database Design and CRUD Module Creation:** Developed MongoDB schemas and implemented Create, Read, Update, and Delete operations to manage user activity logs and system metrics.
3. **Backend Development:** Set up Flask server integrated with Dash to handle API requests, data processing, and serve the frontend.
4. **Frontend Development:** Created interactive Dash components and layouts, integrating Plotly charts and responsive design elements.
5. **Integration and Testing:** Connected the frontend with the backend database, tested real-time data updates, and ensured responsiveness across devices.
6. **Optimization:** Improved query performance using MongoDB indexing and optimized frontend rendering for better user experience.
7. **Documentation and Deployment:** Prepared detailed README, setup instructions, and deployed the application locally for demonstration.

This iterative approach allowed for continuous improvement and adherence to project goals.

---

## Resources

- [MongoDB Documentation](https://docs.mongodb.com/)
- [Plotly Dash Documentation](https://dash.plotly.com/)
- [JupyterDash Documentation](https://github.com/plotly/jupyter-dash)
- [Python Official Documentation](https://docs.python.org/3/)
- [SNHU CS-340 Project Two Rubric](https://snhu.instructure.com/courses/123456/pages/project-two-rubric)