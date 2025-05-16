# Castle Apartments - Final Project

Welcome to **Castle Apartments**, a comprehensive real estate web platform built using **Django**, **PostgreSQL**, and deployed with **Azure**. This system provides users with a modern interface to browse, search, and purchase properties with ease.

---

## Project Overview

Castle Apartments enables users to:
- View and filter available properties
- Edit their profile information and upload profile images
- Submit and finalize purchase offers in a guided process
- Explore seller profiles and property details
- Enjoy extended features like open house listings, inspiration galleries, and favorites

---

## Core Requirements Implemented

- [x] Layout with navigation bar and footer
- [x] Profile page with editable name and profile image upload
- [x] Property catalogue with:
  - Filter by postal code, price, and type
  - Search by street name (case-insensitive)
  - Sort by name and price
- [x] Property detail page with:
  - Full property info, image gallery
  - Seller information with link to seller profile
  - Map showing property location
  - Purchase offer button (submit/resubmit)
- [x] Seller profile with:
  - Conditional display of address for agencies only
  - Logo, cover image, bio
  - List of all properties by the seller
- [x] Submit purchase offers with:
  - Offer price
  - Expiration date
  - Feedback messages on success/failure
- [x] View all submitted purchase offers with:
  - Status tracking (Pending, Accepted, Rejected, Contingent)
  - Finalize link for accepted/contingent offers
- [x] Finalize purchase offer:
  - Step 1: Contact Information (address, national ID, country select)
  - Step 2: Payment Options (Credit Card, Bank Transfer, Mortgage)
  - Step 3: Review (read-only summary)
  - Step 4: Confirmation
  - Persistent data between steps with back/forward navigation

---

## Extra Requirements Implemented

- **Upcoming Open Houses Section**  
  Properties with scheduled viewings are shown on the homepage with time and date.

- **Home Design Inspiration Gallery**  
  A separate section showcasing modern home designs and interiors for user inspiration.

- **Favorite Properties Feature**  
  Users can save properties to a personalized "Favorites" list for quick access.

- **Property Address Map Display**
  Each property detail page shows its location on an interactive map using **Leaflet.js** and **OpenStreetMap**, based on stored latitude and longitude coordinates.

- **Recently Listed Properties Section**  
  Highlights the most recently added properties on the homepage.

- **Popular Properties Section**  
  Displays the most viewed properties based on user clicks/interactions.

---

## Setup Instructions

1. **Install dependencies**:

```bash
pip install -r requirements.txt

---

## Developed By

- Hafdís Arna Guðmundsdóttir  
- Sigríður Embla Jóhannsdóttir 
- Sóllilja Harðardóttir
