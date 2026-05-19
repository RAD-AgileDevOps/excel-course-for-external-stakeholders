-- Table: public.uk_land_registry_price_paid
-- Description: Foundation for "Excel-to-Scale" tutorials. 
-- Includes all 16 standard items from HM Land Registry specifications.

-- This is a comment: Clear existing table if it exists
DROP TABLE IF EXISTS public.uk_land_registry_price_paid;


CREATE TABLE IF NOT EXISTS public.uk_land_registry_price_paid (
    transaction_id uuid PRIMARY KEY,                -- Unique identifier for each sale
    price numeric(15, 2) NOT NULL,                  -- Sale price (Numeric for financial accuracy)
    transfer_date timestamp without time zone,      -- Date when the sale was completed
    postcode varchar(10),                           -- Original postcode at time of transaction
    property_type char(1),                          -- D=Detached, S=Semi, T=Terraced, F=Flats, O=Other
    new_build_flag char(1),                         -- Y = New build, N = Established
    tenure_duration char(1),                        -- F = Freehold, L = Leasehold
    paon text,                                      -- Primary Addressable Object Name (House #/Name)
    saon text,                                      -- Secondary Addressable Object Name (Flat/Unit #)
    street text,                                    -- Street name
    locality text,                                  -- Locality
    town_city text,                                 -- Town or City
    district text,                                  -- District
    county text,                                    -- County
    ppd_category_type char(1),                      -- A = Standard, B = Additional (Repo, BTL, etc.)
    record_status char(1),                          -- A = Addition, C = Change, D = Delete
    
    -- Systems Accountant Metadata
    created_at timestamp DEFAULT now(),
    updated_at timestamp DEFAULT now()
);

-- Adding indices for tutorial performance (illustrating Star Schema logic)
CREATE INDEX idx_lr_postcode ON public.uk_land_registry_price_paid (postcode);
CREATE INDEX idx_lr_transfer_date ON public.uk_land_registry_price_paid (transfer_date);
CREATE INDEX idx_lr_town_city ON public.uk_land_registry_price_paid (town_city);

COMMENT ON TABLE public.uk_land_registry_price_paid IS 'Real-world dataset f' ;