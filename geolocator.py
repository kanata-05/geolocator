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
root.iconbitmap("icon.ico")


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
