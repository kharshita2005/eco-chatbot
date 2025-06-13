from models import db, Product
from app import app

eco_products = [
    {
        "name": "Reusable Bamboo Straw Set",
        "category": "Kitchen",
        "price": 299.00,
        "description": "Eco-friendly bamboo straws with cleaner brush and carry pouch.",
        "image_url": "https://example.com/bamboo-straw.jpg"
    },
    {
        "name": "Organic Cotton Tote Bag",
        "category": "Bags",
        "price": 399.00,
        "description": "Reusable shopping bag made from 100% organic cotton.",
        "image_url": "https://example.com/cotton-tote.jpg"
    },
    {
        "name": "Compostable Garbage Bags",
        "category": "Home Essentials",
        "price": 149.00,
        "description": "Biodegradable garbage bags made from cornstarch.",
        "image_url": "https://example.com/compost-bags.jpg"
    },
    {
        "name": "Plantable Seed Pencils",
        "category": "Stationery",
        "price": 199.00,
        "description": "Pencils that grow into herbs or flowers once used.",
        "image_url": "https://example.com/seed-pencil.jpg"
    },
    {
        "name": "Solar-Powered LED Garden Lights",
        "category": "Outdoor",
        "price": 899.00,
        "description": "Energy-efficient solar lights for garden decoration.",
        "image_url": "https://example.com/solar-lights.jpg"
    },
    {
        "name": "Bamboo Toothbrush Set",
        "category": "Personal Care",
        "price": 249.00,
        "description": "Set of biodegradable bamboo toothbrushes with soft bristles.",
        "image_url": "https://example.com/bamboo-toothbrush.jpg"
    },
    {
        "name": "Recycled Paper Notebooks",
        "category": "Stationery",
        "price": 299.00,
        "description": "Notebooks made from 100% recycled paper.",
        "image_url": "https://example.com/recycled-notebook.jpg"
    },
    {
        "name": "Eco-Friendly Yoga Mat",
        "category": "Fitness",
        "price": 1299.00,
        "description": "Non-toxic, biodegradable yoga mat made from natural rubber.",
        "image_url": "https://example.com/yoga-mat.jpg"
    },
    {
        "name": "Reusable Beeswax Food Wraps",
        "category": "Kitchen",
        "price": 499.00,
        "description": "Sustainable alternative to plastic wrap, made from beeswax.",
        "image_url": "https://example.com/beeswax-wrap.jpg"
    },
    {
        "name": "Eco-Friendly Phone Case",
        "category": "Electronics Accessories",
        "price": 799.00,
        "description": "Biodegradable phone case made from plant-based materials.",
        "image_url": "https://example.com/eco-phone-case.jpg"
    },
    {
        "name": "Natural Soy Wax Candles",
        "category": "Home Decor",
        "price": 499.00,
        "description": "Hand-poured candles made from natural soy wax with essential oils.",
        "image_url": "https://example.com/soy-candle.jpg"
    },
    {
        "name": "Eco-Friendly Laundry Detergent Sheets",
        "category": "Laundry",
        "price": 399.00,
        "description": "Concentrated laundry detergent sheets that dissolve in water.",
        "image_url": "https://example.com/laundry-sheets.jpg"
    },
    {
        "name": "Sustainable Wooden Sunglasses",
        "category": "Accessories",
        "price": 1499.00,
        "description": "Stylish sunglasses made from sustainable wood.",
        "image_url": "https://example.com/wooden-sunglasses.jpg"
    },
    {
        "name": "Biodegradable Phone Charger",
        "category": "Electronics Accessories",
        "price": 899.00,
        "description": "Eco-friendly phone charger made from biodegradable materials.",
        "image_url": "https://example.com/biodegradable-charger.jpg"
    },
    {
        "name": "Organic Herbal Tea Set",
        "category": "Beverages",
        "price": 599.00,
        "description": "Assorted organic herbal teas in eco-friendly packaging.",
        "image_url": "https://example.com/herbal-tea-set.jpg"
    },
    {
        "name": "Recycled Glass Water Bottle",
        "category": "Kitchen",
        "price": 699.00,
        "description": "Stylish water bottle made from recycled glass with a silicone sleeve.",
        "image_url": "https://example.com/recycled-glass-bottle.jpg"
    },
    {
        "name": "Eco-Friendly Pet Toys",
        "category": "Pet Supplies",
        "price": 349.00,
        "description": "Durable pet toys made from natural, non-toxic materials.",
        "image_url": "https://example.com/eco-pet-toys.jpg"
    },
    {
        "name": "Sustainable Travel Utensil Set",
        "category": "Travel Accessories",
        "price": 399.00,
        "description": "Portable utensil set made from bamboo, perfect for on-the-go meals.",
        "image_url": "https://example.com/travel-utensil-set.jpg"
    },
    {
        "name": "Eco-Friendly Air Purifying Bag",
        "category": "Home Essentials",
        "price": 499.00,
        "description": "Activated charcoal bag that purifies air and removes odors naturally.",
        "image_url": "https://example.com/air-purifying-bag.jpg"
    },
    {
        "name": "Natural Jute Rug",
        "category": "Home Decor",
        "price": 1999.00,
        "description": "Handwoven jute rug that adds a rustic touch to your home.",
        "image_url": "https://example.com/jute-rug.jpg"
    },
    {
        "name": "Eco-Friendly Reusable Cutlery Set",
        "category": "Kitchen",
        "price": 299.00,
        "description": "Portable cutlery set made from stainless steel and bamboo.",
        "image_url": "https://example.com/reusable-cutlery.jpg"
    },
    {
        "name": "Biodegradable Glitter",
        "category": "Craft Supplies",
        "price": 199.00,
        "description": "Eco-friendly glitter made from plant cellulose, perfect for crafts.",
        "image_url": "https://example.com/biodegradable-glitter.jpg"
    },
    {
        "name": "Sustainable Cork Yoga Block",
        "category": "Fitness",
        "price": 499.00,
        "description": "Yoga block made from sustainable cork, providing stability and support.",
        "image_url": "https://example.com/cork-yoga-block.jpg"
    },
    {
        "name": "Organic Cotton Bath Towels",
        "category": "Home Essentials",
        "price": 899.00,
        "description": "Soft and absorbent bath towels made from 100% organic cotton.",
        "image_url": "https://example.com/organic-cotton-towels.jpg"
    },
    {
        "name": "Eco-Friendly Reusable Food Storage Bags",
        "category": "Kitchen",
        "price": 349.00,
        "description": "Silicone food storage bags that are reusable and dishwasher safe.",
        "image_url": "https://example.com/reusable-food-bags.jpg"
    },
    {
        "name": "Natural Coconut Bowls",
        "category": "Kitchen",
        "price": 499.00,
        "description": "Handcrafted bowls made from reclaimed coconut shells.",
        "image_url": "https://example.com/coconut-bowls.jpg"
    },
    {
        "name": "Eco-Friendly Reusable Coffee Cup",
        "category": "Beverages",
        "price": 399.00,
        "description": "Sustainable coffee cup made from bamboo fiber and silicone.",
        "image_url": "https://example.com/reusable-coffee-cup.jpg"
    },
    {
        "name": "Sustainable Wooden Phone Stand",
        "category": "Electronics Accessories",
        "price": 299.00,
        "description": "Stylish phone stand made from sustainable wood.",
        "image_url": "https://example.com/wooden-phone-stand.jpg"
    },
    {
        "name": "Organic Cotton Face Masks",
        "category": "Personal Care",
        "price": 199.00,
        "description": "Reusable face masks made from soft organic cotton.",
        "image_url": "https://example.com/organic-face-masks.jpg"
    },
    {
        "name": "Eco-Friendly Reusable Sandwich Wraps",
        "category": "Kitchen",
        "price": 249.00,
        "description": "Beeswax wraps for wrapping sandwiches and snacks, reusable and washable.",
        "image_url": "https://example.com/sandwich-wraps.jpg"
    },
    {
        "name": "Sustainable Travel Toiletry Kit",
        "category": "Travel Accessories",
        "price": 499.00,
        "description": "Compact toiletry kit made from recycled materials, perfect for travel.",
        "image_url": "https://example.com/travel-toiletry-kit.jpg"
    },
    {
        "name": "Natural Wool Dryer Balls",
        "category": "Laundry",
        "price": 299.00,
        "description": "Reusable wool dryer balls that reduce drying time and soften clothes naturally.",
        "image_url": "https://example.com/wool-dryer-balls.jpg"
    },
    {
        "name": "Eco-Friendly Reusable Produce Bags",
        "category": "Kitchen",
        "price": 199.00,
        "description": "Set of reusable mesh produce bags for grocery shopping.",
        "image_url": "https://example.com/reusable-produce-bags.jpg"
    },
    {
        "name": "Sustainable Wooden Coasters",
        "category": "Home Decor",
        "price": 399.00,
        "description": "Handcrafted coasters made from reclaimed wood, perfect for protecting surfaces.",
        "image_url": "https://example.com/wooden-coasters.jpg"
    },
    {
        "name": "Organic Herbal Bath Soak",
        "category": "Personal Care",
        "price": 499.00,
        "description": "Relaxing bath soak made from organic herbs and essential oils.",
        "image_url": "https://example.com/herbal-bath-soak.jpg"
    },
    {
        "name": "Eco-Friendly Reusable Makeup Remover Pads",
        "category": "Personal Care",
        "price": 249.00,
        "description": "Soft, washable pads for removing makeup, reducing waste.",
        "image_url": "https://example.com/makeup-remover-pads.jpg"
    },
    {
        "name": "Sustainable Cork Yoga Mat",
        "category": "Fitness",
        "price": 1599.00,
        "description": "Eco-friendly yoga mat made from natural cork and rubber.",
        "image_url": "https://example.com/cork-yoga-mat.jpg"
    },
    {
        "name": "Organic Cotton Dish Towels",
        "category": "Kitchen",
        "price": 399.00,
        "description": "Set of absorbent dish towels made from organic cotton.",
        "image_url": "https://example.com/organic-dish-towels.jpg"
    },
    {
        "name": "Biodegradable Glitter Gel",
        "category": "Craft Supplies",
        "price": 299.00,
        "description": "Eco-friendly glitter gel for crafts, made from plant-based materials.",
        "image_url": "https://example.com/biodegradable-glitter-gel.jpg"
    },
    {
        "name": "Sustainable Wooden Keychain",
        "category": "Accessories",
        "price": 199.00,
        "description": "Handcrafted keychain made from sustainable wood.",
        "image_url": "https://example.com/wooden-keychain.jpg"
    },
    {
        "name": "Eco-Friendly Reusable Snack Bags",
        "category": "Kitchen",
        "price": 249.00,
        "description": "Silicone snack bags that are reusable and dishwasher safe.",
        "image_url": "https://example.com/reusable-snack-bags.jpg"
    },
    {
        "name": "Natural Coconut Soap Bars",
        "category": "Personal Care",
        "price": 299.00,
        "description": "Handmade soap bars made from natural coconut oil.",
        "image_url": "https://example.com/coconut-soap-bars.jpg"
    },
    {
        "name": "Sustainable Wooden Serving Tray",
        "category": "Home Decor",
        "price": 899.00,
        "description": "Elegant serving tray made from reclaimed wood.",
        "image_url": "https://example.com/wooden-serving-tray.jpg"
    },
    {
        "name": "Organic Cotton Reusable Coffee Filters",
        "category": "Kitchen",
        "price": 199.00,
        "description": "Set of reusable coffee filters made from organic cotton.",
        "image_url": "https://example.com/organic-coffee-filters.jpg"
    },
    {
        "name": "Eco-Friendly Reusable Water Balloons",
        "category": "Outdoor",
        "price": 349.00,
        "description": "Silicone water balloons that can be reused, perfect for summer fun.",
        "image_url": "https://example.com/reusable-water-balloons.jpg"
    },
    {
        "name": "Sustainable Wooden Desk Organizer",
        "category": "Office Supplies",
        "price": 599.00,
        "description": "Stylish desk organizer made from sustainable wood.",
        "image_url": "https://example.com/wooden-desk-organizer.jpg"
    },
    {
        "name": "Natural Wool Felt Coasters",
        "category": "Home Decor",
        "price": 299.00,
        "description": "Handcrafted coasters made from natural wool felt.",
        "image_url": "https://example.com/wool-felt-coasters.jpg"
    },
    {
        "name": "Eco-Friendly Reusable Food Covers",
        "category": "Kitchen",
        "price": 249.00,
        "description": "Set of silicone food covers that are reusable and stretchable.",
        "image_url": "https://example.com/reusable-food-covers.jpg"
    },
    {
        "name": "Sustainable Wooden Phone Case",
        "category": "Electronics Accessories",
        "price": 899.00,
        "description": "Stylish phone case made from sustainable wood.",
        "image_url": "https://example.com/wooden-phone-case.jpg"
    },
    {
        "name": "Organic Cotton Produce Bags",
        "category": "Kitchen",
        "price": 299.00,
        "description": "Set of reusable produce bags made from organic cotton.",
        "image_url": "https://example.com/organic-produce-bags.jpg"
    },
    {
        "name": "Eco-Friendly Reusable Straws",
        "category": "Kitchen",
        "price": 199.00,
        "description": "Set of stainless steel straws with a cleaning brush and pouch.",
        "image_url": "https://example.com/reusable-straws.jpg"
    },
    {
        "name": "Natural Jute Shopping Bag",
        "category": "Bags",
        "price": 399.00,
        "description": "Durable shopping bag made from natural jute fibers.",
        "image_url": "https://example.com/jute-shopping-bag.jpg"
    },
    {
        "name": "Sustainable Wooden Watch",
        "category": "Accessories",
        "price": 1999.00,
        "description": "Stylish watch made from sustainable wood with a minimalist design.",
        "image_url": "https://example.com/wooden-watch.jpg"
    },
    {
        "name": "Organic Cotton Bathrobe",
        "category": "Personal Care",
        "price": 2499.00,
        "description": "Luxurious bathrobe made from 100% organic cotton.",
        "image_url": "https://example.com/organic-bathrobe.jpg"
    },
    {
        "name": "Eco-Friendly Reusable Food Wraps",
        "category": "Kitchen",
        "price": 399.00,
        "description": "Beeswax wraps for covering food, reusable and washable.",
        "image_url": "https://example.com/reusable-food-wraps.jpg"
    },
    {
        "name": "Sustainable Wooden Key Holder",
        "category": "Home Decor",
        "price": 499.00,
        "description": "Handcrafted key holder made from reclaimed wood.",
        "image_url": "https://example.com/wooden-key-holder.jpg"
    },
    {
        "name": "Natural Coconut Fiber Doormat",
        "category": "Home Essentials",
        "price": 799.00,
        "description": "Durable doormat made from natural coconut fibers.",
        "image_url": "https://example.com/coconut-fiber-doormat.jpg"
    },
    {
        "name": "Eco-Friendly Reusable Snack Containers",
        "category": "Kitchen",
        "price": 349.00,
        "description": "Set of silicone snack containers that are reusable and dishwasher safe.",
        "image_url": "https://example.com/reusable-snack-containers.jpg"
    },
    {
        "name": "Sustainable Wooden Coatrack",
        "category": "Home Decor",
        "price": 899.00,
        "description": "Stylish coatrack made from reclaimed wood.",
        "image_url": "https://example.com/wooden-coatrack.jpg"
    },
    {
        "name": "Organic Cotton Yoga Towel",
        "category": "Fitness",
        "price": 599.00,
        "description": "Soft and absorbent yoga towel made from organic cotton.",
        "image_url": "https://example.com/organic-yoga-towel.jpg"
    },
    {
        "name": "Eco-Friendly Reusable Food Jars",
        "category": "Kitchen",
        "price": 499.00,
        "description": "Glass food jars with bamboo lids, perfect for storing dry goods.",
        "image_url": "https://example.com/reusable-food-jars.jpg"
    },
    {
        "name": "Sustainable Wooden Candle Holders",
        "category": "Home Decor",
        "price": 399.00,
        "description": "Elegant candle holders made from reclaimed wood.",
        "image_url": "https://example.com/wooden-candle-holders.jpg"
    },
    {
        "name": "Natural Wool Felt Laptop Sleeve",
        "category": "Electronics Accessories",
        "price": 799.00,
        "description": "Protective laptop sleeve made from natural wool felt.",
        "image_url": "https://example.com/wool-felt-laptop-sleeve.jpg"
    },
    {
        "name": "Eco-Friendly Reusable Food Storage Containers",
        "category": "Kitchen",
        "price": 599.00,
        "description": "Set of silicone food storage containers that are reusable and dishwasher safe.",
        "image_url": "https://example.com/reusable-food-storage-containers.jpg"
    },
    {
        "name": "Sustainable Wooden Bookmarks",
        "category": "Stationery",
        "price": 199.00,
        "description": "Handcrafted bookmarks made from sustainable wood.",
        "image_url": "https://example.com/wooden-bookmarks.jpg"
    },
    {
        "name": "Organic Cotton Hair Towels",
        "category": "Personal Care",
        "price": 399.00,
        "description": "Soft hair towels made from 100% organic cotton.",
        "image_url": "https://example.com/organic-hair-towels.jpg"
    },
    {
        "name": "Eco-Friendly Reusable Baking Mats",
        "category": "Kitchen",
        "price": 299.00,
        "description": "Silicone baking mats that are reusable and non-stick.",
        "image_url": "https://example.com/reusable-baking-mats.jpg"
    },
    {
        "name": "Sustainable Wooden Picture Frames",
        "category": "Home Decor",
        "price": 499.00,
        "description": "Elegant picture frames made from reclaimed wood.",
        "image_url": "https://example.com/wooden-picture-frames.jpg"
    },
    {
        "name": "Natural Jute Storage Baskets",
        "category": "Home Essentials",
        "price": 699.00,
        "description": "Handwoven storage baskets made from natural jute fibers.",
        "image_url": "https://example.com/jute-storage-baskets.jpg"
    },
    {
        "name": "Eco-Friendly Reusable Food Pouches",
        "category": "Kitchen",
        "price": 249.00,
        "description": "Silicone food pouches that are reusable and dishwasher safe.",
        "image_url": "https://example.com/reusable-food-pouches.jpg"
    },
    {
        "name": "Sustainable Wooden Serving Spoons",
        "category": "Kitchen",
        "price": 399.00,
        "description": "Handcrafted serving spoons made from sustainable wood.",
        "image_url": "https://example.com/wooden-serving-spoons.jpg"
    },
    {
        "name": "Organic Cotton Hair Wraps",
        "category": "Personal Care",
        "price": 299.00,
        "description": "Soft hair wraps made from 100% organic cotton.",
        "image_url": "https://example.com/organic-hair-wraps.jpg"
    },
    {
        "name": "Eco-Friendly Reusable Food Bags",
        "category": "Kitchen",
        "price": 349.00,
        "description": "Set of silicone food bags that are reusable and dishwasher safe.",
        "image_url": "https://example.com/reusable-food-bags.jpg"
    },
    {
        "name": "Sustainable Wooden Wall Clock",
        "category": "Home Decor",
        "price": 999.00,
        "description": "Elegant wall clock made from reclaimed wood.",
        "image_url": "https://example.com/wooden-wall-clock.jpg"
    },
    {
        "name": "Natural Wool Felt Pencil Case",
        "category": "Stationery",
        "price": 399.00,
        "description": "Stylish pencil case made from natural wool felt.",
        "image_url": "https://example.com/wool-felt-pencil-case.jpg"
    },
    {
        "name": "Eco-Friendly Reusable Baking Cups",
        "category": "Kitchen",
        "price": 249.00,
        "description": "Silicone baking cups that are reusable and non-stick.",
        "image_url": "https://example.com/reusable-baking-cups.jpg"
    },
    {
        "name": "Sustainable Wooden Key Organizer",
        "category": "Home Decor",
        "price": 499.00,
        "description": "Handcrafted key organizer made from reclaimed wood.",
        "image_url": "https://example.com/wooden-key-organizer.jpg"
    },
    {
        "name": "Organic Cotton Hair Scrunchies",
        "category": "Personal Care",
        "price": 199.00,
        "description": "Soft hair scrunchies made from 100% organic cotton.",
        "image_url": "https://example.com/organic-hair-scrunchies.jpg"
    },
    {
        "name": "Eco-Friendly Reusable Food Wraps Set",
        "category": "Kitchen",
        "price": 399.00,
        "description": "Set of beeswax wraps for covering food, reusable and washable.",
        "image_url": "https://example.com/reusable-food-wraps-set.jpg"
    },
    {
        "name": "Sustainable Wooden Serving Board",
        "category": "Kitchen",
        "price": 799.00,
        "description": "Elegant serving board made from reclaimed wood.",
        "image_url": "https://example.com/wooden-serving-board.jpg"
    },
    {
        "name": "Natural Jute Plant Hangers",
        "category": "Home Decor",
        "price": 299.00,
        "description": "Handwoven plant hangers made from natural jute fibers.",
        "image_url": "https://example.com/jute-plant-hangers.jpg"
    },
    {
        "name": "Eco-Friendly Reusable Food Storage Wraps",
        "category": "Kitchen",
        "price": 249.00,
        "description": "Set of silicone food wraps that are reusable and stretchable.",
        "image_url": "https://example.com/reusable-food-storage-wraps.jpg"
    },
    {
        "name": "Sustainable Wooden Coasters Set",
        "category": "Home Decor",
        "price": 399.00,
        "description": "Set of handcrafted coasters made from sustainable wood.",
        "image_url": "https://example.com/wooden-coasters-set.jpg"
    },
    {
        "name": "Organic Cotton Hair Towel Wrap",
        "category": "Personal Care",
        "price": 399.00,
        "description": "Soft hair towel wrap made from 100% organic cotton.",
        "image_url": "https://example.com/organic-hair-towel-wrap.jpg"
    },
    {
        "name": "Eco-Friendly Reusable Food Containers Set",
        "category": "Kitchen",
        "price": 599.00,
        "description": "Set of silicone food containers that are reusable and dishwasher safe.",
        "image_url": "https://example.com/reusable-food-containers-set.jpg"
    },
    {
        "name": "Sustainable Wooden Serving Utensils",
        "category": "Kitchen",
        "price": 399.00,
        "description": "Handcrafted serving utensils made from sustainable wood.",
        "image_url": "https://example.com/wooden-serving-utensils.jpg"
    },
    {
        "name": "Natural Wool Felt Keychain",
        "category": "Accessories",
        "price": 199.00,
        "description": "Stylish keychain made from natural wool felt.",
        "image_url": "https://example.com/wool-felt-keychain.jpg"
    },
    {
        "name": "Eco-Friendly Reusable Food Storage Bags Set",
        "category": "Kitchen",
        "price": 349.00,
        "description": "Set of silicone food storage bags that are reusable and dishwasher safe.",
        "image_url": "https://example.com/reusable-food-storage-bags-set.jpg"
    },
    {
        "name": "Sustainable Wooden Wall Shelf",
        "category": "Home Decor",
        "price": 899.00,
        "description": "Elegant wall shelf made from reclaimed wood.",
        "image_url": "https://example.com/wooden-wall-shelf.jpg"
    },
    {
        "name": "Organic Cotton Hair Bands",
        "category": "Personal Care",
        "price": 199.00,
        "description": "Soft hair bands made from 100% organic cotton.",
        "image_url": "https://example.com/organic-hair-bands.jpg"
    },
    {
        "name": "Eco-Friendly Reusable Baking Sheets",
        "category": "Kitchen",
        "price": 299.00,
        "description": "Silicone baking sheets that are reusable and non-stick.",
        "image_url": "https://example.com/reusable-baking-sheets.jpg"
    },
    {
        "name": "Sustainable Wooden Jewelry Box",
        "category": "Accessories",
        "price": 1299.00,
        "description": "Elegant jewelry box made from reclaimed wood.",
        "image_url": "https://example.com/wooden-jewelry-box.jpg"
    },
    {
        "name": "Natural Jute Wall Hanging",
        "category": "Home Decor",
        "price": 499.00,
        "description": "Handwoven wall hanging made from natural jute fibers.",
        "image_url": "https://example.com/jute-wall-hanging.jpg"
    },
    {
        "name": "Eco-Friendly Reusable Food Storage Bags",
        "category": "Kitchen",
        "price": 249.00,
        "description": "Set of silicone food storage bags that are reusable and dishwasher safe.",
        "image_url": "https://example.com/reusable-food-storage-bags.jpg"
    },
    {
        "name": "Sustainable Wooden Keychain Holder",
        "category": "Home Decor",
        "price": 399.00,
        "description": "Handcrafted keychain holder made from reclaimed wood.",
        "image_url": "https://example.com/wooden-keychain-holder.jpg"
    },
    {
        "name": "Organic Cotton Hair Clips",
        "category": "Personal Care",
        "price": 199.00,
        "description": "Soft hair clips made from 100% organic cotton.",
        "image_url": "https://example.com/organic-hair-clips.jpg"
    },
    {
        "name": "Eco-Friendly Reusable Food Storage Wraps Set",
        "category": "Kitchen",
        "price": 399.00,
        "description": "Set of beeswax wraps for covering food, reusable and washable.",
        "image_url": "https://example.com/reusable-food-storage-wraps-set.jpg"
    },
    {
        "name": "Sustainable Wooden Serving Tray Set",
        "category": "Kitchen",
        "price": 899.00,
        "description": "Elegant serving tray set made from reclaimed wood.",
        "image_url": "https://example.com/wooden-serving-tray-set.jpg"
    },
    {
        "name": "Natural Jute Plant Pots",
        "category": "Home Decor",
        "price": 299.00,
        "description": "Handwoven plant pots made from natural jute fibers.",
        "image_url": "https://example.com/jute-plant-pots.jpg"
    },
    {
        "name": "Eco-Friendly Reusable Food Storage Bags Set",
        "category": "Kitchen",
        "price": 349.00,
        "description": "Set of silicone food storage bags that are reusable and dishwasher safe.",
        "image_url": "https://example.com/reusable-food-storage-bags-set.jpg"
    },
    {
        "name": "Sustainable Wooden Coatrack",
        "category": "Home Decor",
        "price": 899.00,
        "description": "Stylish coatrack made from reclaimed wood.",
        "image_url": "https://example.com/wooden-coatrack.jpg"
    },
    {
        "name": "Organic Cotton Hair Ties",
        "category": "Personal Care",
        "price": 199.00,
        "description": "Soft hair ties made from 100% organic cotton.",
        "image_url": "https://example.com/organic-hair-ties.jpg"
    },
    {
        "name": "Eco-Friendly Reusable Baking Mats Set",
        "category": "Kitchen",
        "price": 299.00,
        "description": "Set of silicone baking mats that are reusable and non-stick.",
        "image_url": "https://example.com/reusable-baking-mats-set.jpg"
    },
    {
        "name": "Sustainable Wooden Jewelry Organizer",
        "category": "Accessories",
        "price": 1299.00,
        "description": "Elegant jewelry organizer made from reclaimed wood.",
        "image_url": "https://example.com/wooden-jewelry-organizer.jpg"
    },
    {
        "name": "Natural Jute Storage Bags",
        "category": "Home Essentials",
        "price": 699.00,
        "description": "Handwoven storage bags made from natural jute fibers.",
        "image_url": "https://example.com/jute-storage-bags.jpg"
    },
]

with app.app_context():
    for product in eco_products:
        new_product = Product(
            name=product["name"],
            category=product["category"],
            price=product["price"],
            description=product["description"],
            image_url=product["image_url"]
        )
        db.session.add(new_product)
    db.session.commit()
    print("✅ Inventory seeded with eco-friendly products.")
