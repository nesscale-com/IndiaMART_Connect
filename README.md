# ERPNext IndiaMART Integration

## Overview

This integration allows you to import leads from IndiaMART into ERPNext. It fetches leads every 5 minutes, with an option to fetch custom leads, and ensures no duplicates using the `query_id`.

## Installation

```bash
# Step 1: Clone the IndiaMART Connect app
bench get-app indiaMART_connect

# Step 2: Install the app for your ERPNext site
bench --site site_name install-app indiaMART_connect

```

## Configuration

1. Access the integration settings.

2. Enter your IndiaMART API credentials.


## Usage

1. The integration fetches leads from IndiaMART every 5 Minutes.

2. It checks for duplicate leads using query_id.

3. New leads are added to ERPNext.

4. All activities are logged.

## Troubleshooting

Check integration logs for errors and consult IndiaMART API documentation for updates.

## Support

Contact [info@nesscale.com](mailto:info@nesscale.com) for assistance.

## License

This integration is under the MIT License.

