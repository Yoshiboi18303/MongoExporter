# MongoExporter

An easy way to have your MongoDB data exported to a CSV format!

## Usage

### Prerequisites

**[Python v3](https://python.org/)**

**[Git](https://git-scm.com)**

### Step 1

First, clone the repository:

```bash
git clone https://github.com/Yoshiboi18303/MongoExporter
cd MongoExporter
```

### Step 2

Next, install the dependencies:

```bash
pip install -r requirements.txt
```

This will install the dependencies listed in the `requirements.txt` file, which will ensure you're ready to use the script.

### Step 3

Then, open the `config.jsonc` file, which houses the configuration for the script.

Replace all the placeholders with the actual values _(e.g. `connectionString` should be your MongoDB connection string from MongoDB Atlas)_.

### Step 4

Afterwards, run the script.

```bash
python main.py
```

### Step 5 _(optional)_

If you have more than one collection you need the data from, replace `collection` with that value, then run the script again.

Rinse and repeat steps **[4](#step-4)** and **[5](#step-5-optional)** until you have all the data you need.
