# IP Geolocator

IP Geolocator is a versatile tool designed to retrieve detailed geographical information about any given IP address. Utilizing advanced IP geolocation APIs, it provides comprehensive data including country, region, city, latitude, longitude, ISP, and more. This tool is invaluable for network administrators, security analysts, marketers, and anyone needing precise IP address location information.

## Features

### Comprehensive Geolocation Information
- **Country Detection**: Identify the country associated with the IP address.
- **Region/State**: Determine the specific region or state.
- **City**: Discover the city where the IP address is located.
- **Latitude and Longitude**: Provide exact geographical coordinates.
- **ISP Information**: Identify the Internet Service Provider (ISP).
- **Time Zone**: Determine the timezone of the location.
- **Postal Code**: Retrieve the postal code.
- **ASN**: Autonomous System Number details.

### Multi-Source Data Integration
- **API Support**: Fetch data from various IP geolocation APIs for enhanced accuracy.
- **Fallback Mechanism**: Ensure data retrieval even if primary sources fail.

### User-Friendly Graphical Interface (GUI)
- **Input IP Address**: Enter the IP address to lookup.
- **Get Geolocation**: Click a button to retrieve and display detailed information.
- **Visual Feedback**: Results are displayed in a user-friendly format within the GUI.

### Advanced Features
- **Historical Data**: Access historical geolocation data.
- **Customization**: Tailor settings to suit specific needs.

## Installation and Usage

### Prerequisites
- Python 3.x
- `requests` library
- Tkinter (standard Python library for GUI)

### Installation Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/ip-geolocator.git
   cd ip-geolocator
   ```

2. **Install Required Libraries**

   Ensure you have the `requests` library installed:

   ```bash
   pip install requests
   ```

### Running the Application

1. **Launch the GUI**

   Run the script to open the graphical user interface (GUI):

   ```bash
   python ip_geolocator.py
   ```

2. **Using the GUI**

   - **Enter IP Address**: Input the IP address you want to geolocate.
   - **Get Geolocation**: Click the "Get Geolocation" button to fetch and display detailed information about the IP address.

3. **Customization**

   - Extend the functionality by integrating additional geolocation APIs.
   - Enhance the GUI with more features such as map visualization or bulk IP lookup capabilities.

## Example

Here’s a simplified version of the GUI script:

```python
import tkinter as tk
import requests

def get_geolocation():
    ip_address = ip_entry.get()
    url = f"https://ipwho.is/{ip_address}"
    response = requests.get(url)
    data = response.json()
    
    if 'error' in data:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Error: {data['error']}")
    else:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"IP: {data.get('ip', 'N/A')}\n")
        result_text.insert(tk.END, f"Type: {data.get('type', 'N/A')}\n")
        result_text.insert(tk.END, f"Continent: {data.get('continent', 'N/A')}\n")
        result_text.insert(tk.END, f"Country: {data.get('country', 'N/A')}\n")
        result_text.insert(tk.END, f"Region: {data.get('region', 'N/A')}\n")
        result_text.insert(tk.END, f"City: {data.get('city', 'N/A')}\n")
        result_text.insert(tk.END, f"Latitude: {data.get('latitude', 'N/A')}\n")
        result_text.insert(tk.END, f"Longitude: {data.get('longitude', 'N/A')}\n")
        result_text.insert(tk.END, f"Postal Code: {data.get('postal', 'N/A')}\n")
        result_text.insert(tk.END, f"Calling Code: {data.get('calling_code', 'N/A')}\n")
        result_text.insert(tk.END, f"Capital: {data.get('capital', 'N/A')}\n")
        result_text.insert(tk.END, f"ASN: {data['connection'].get('asn', 'N/A')}\n")
        result_text.insert(tk.END, f"Organization: {data['connection'].get('org', 'N/A')}\n")
        result_text.insert(tk.END, f"ISP: {data['connection'].get('isp', 'N/A')}\n")
        result_text.insert(tk.END, f"Domain: {data['connection'].get('domain', 'N/A')}\n")
        result_text.insert(tk.END, f"Timezone: {data['timezone'].get('id', 'N/A')}\n")
        result_text.insert(tk.END, f"Timezone Abbreviation: {data['timezone'].get('abbr', 'N/A')}\n")
        result_text.insert(tk.END, f"Current Time: {data['timezone'].get('current_time', 'N/A')}\n")

# Create main window
root = tk.Tk()
root.title("IP Geolocator")
root.configure(bg='#202124')  # Dark theme background color

# IP address entry
ip_label = tk.Label(root, text="Enter IP Address:", bg='#202124', fg='white')
ip_label.pack()
ip_entry = tk.Entry(root)
ip_entry.pack(pady=3)

# Button to get geolocation
get_location_button = tk.Button(root, text="Get Geolocation", command=get_geolocation, bg='#37474f', fg='white')
get_location_button.pack()

# Display results
result_text = tk.Text(root, height=20, width=60, bg='#2a2d2e', fg='white')
result_text.pack()

root.mainloop()
```

### Explanation

- **get_geolocation()**: Fetches geolocation data from the `ipwho.is` API and displays it in the text area.
- **GUI Elements**: Includes an input field for IP address, a button to trigger geolocation, and a text area to display results.

## Contributing

Contributions are welcome! For suggestions, improvements, or bug fixes, please open an issue or submit a pull request following our [contributing guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or need further assistance, feel free to contact us at [krishkracks@gmail.com](mailto:krishkracks@gmail.com) or open an issue on this repository.

---

