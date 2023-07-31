# Car Showroom Web Application

This is a web application built using Django that allows users to explore various car showrooms, view available car brands and models, and see details about individual cars.

## Features

- **Showroom Listing:** Users can view a list of all available car showrooms. Each showroom displays its name, location, and a representative picture.

- **Showroom Details:** When users click on a showroom from the listing, they are taken to a showroom detail page where they can see more information about the showroom, including its staff members and the brands it represents.

- **Brands and Models:** On the showroom detail page, users can see a list of all the car brands associated with the showroom. When they click on a brand, a dropdown appears showing all the models available for that brand.

- **Car Listing:** Users can view a list of cars for a selected model. The car listing page displays important details about each car, including its VIN, price, year, picture, and a list of features.

## Setup Instructions

To run this project locally, follow these steps:

1. Clone the repository to your local machine using `git clone <repository_url>`.

2. Create a virtual environment and activate it.

3. Install the required dependencies using `pip install -r requirements.txt`.

4. Apply the database migrations using `python manage.py migrate`.

5. Create a superuser using `python manage.py createsuperuser`. This will allow you to access the Django admin panel.

6. Load sample data into the database using `python manage.py loaddata sample_data.json`.

7. Run the development server using `python manage.py runserver`.

8. Open your web browser and go to `http://localhost:8000` to access the application.

## Admin Panel

To access the Django admin panel, go to `http://localhost:8000/admin` and log in using the superuser credentials you created earlier. From the admin panel, you can manage the data for showrooms, staff, brands, models, and cars.

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute the code as you see fit. See the [LICENSE](LICENSE) file for more details.
