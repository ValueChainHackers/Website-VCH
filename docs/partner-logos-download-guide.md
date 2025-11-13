# Partner Logos Download Guide

This guide provides direct links to download the official logos for VCH partners.

## Required Logos

### 1. Scania
**Recommended Source:** World Vector Logo or SeekLogo
- **SVG Download:** https://worldvectorlogo.com/logo/scania-3
- **Alternative:** https://seeklogo.com/vector-logo/123303/scania
- **Format Needed:** SVG or high-res PNG
- **Save as:** `assets/images/partners/scania-logo.svg`

### 2. Puma
**Recommended Source:** World Vector Logo or SeekLogo
- **SVG Download:** https://worldvectorlogo.com/logo/puma-logo
- **Alternative:** https://seeklogo.com/vector-logo/112829/puma
- **Format Needed:** SVG or high-res PNG
- **Save as:** `assets/images/partners/puma-logo.svg`

### 3. Danone
**Recommended Source:** World Vector Logo or Brandfetch
- **SVG Download:** https://worldvectorlogo.com/logo/danone
- **Alternative:** https://brandfetch.com/danone.com
- **Format Needed:** SVG or high-res PNG
- **Save as:** `assets/images/partners/danone-logo.svg`

### 4. Evofenedx
**Challenge:** This is likely a smaller organization, may require:
- Check official website: https://evofenedex.nl/
- Contact them directly for logo usage permission
- Download from their press/media kit
- **Save as:** `assets/images/partners/evofenedx-logo.svg` (note: correct spelling is "Evofenedex")

### 5. Windesheim University
**Status:** ✅ Already have this logo
- Location: `assets/images/partners/windesheim-logo.webp`

## Download Instructions

### Option 1: Manual Download
1. Visit each URL above
2. Click download button for SVG format (preferred) or PNG
3. Save to `assets/images/partners/` directory
4. Rename to match the naming convention above

### Option 2: Using wget/curl
```bash
# Example for downloading (adjust URLs as needed)
cd assets/images/partners/

# Download Scania
wget https://[direct-download-url] -O scania-logo.svg

# Download Puma
wget https://[direct-download-url] -O puma-logo.svg

# Download Danone
wget https://[direct-download-url] -O danone-logo.svg
```

## After Downloading

### Convert to WebP (Optional)
For optimal web performance, convert to WebP format:

```bash
# Using cwebp tool
cwebp -q 80 scania-logo.png -o scania-logo.webp
cwebp -q 80 puma-logo.png -o puma-logo.webp
cwebp -q 80 danone-logo.png -o danone-logo.webp
cwebp -q 80 evofenedx-logo.png -o evofenedx-logo.webp
```

Or use online tools like:
- https://convertio.co/png-webp/
- https://cloudconvert.com/png-to-webp

### Update index.html

The logos are already referenced in index.html lines 86-90. Once you download and save the files, they should automatically appear on the website.

## Legal Considerations

- ✅ **Educational/Non-profit use:** Usually acceptable for partner logos on academic website
- ✅ **Attribution:** Partners section already attributes correctly
- ⚠️ **Commercial use:** Ensure partnership agreements allow logo usage
- 📧 **Best practice:** Request logos directly from partners' marketing departments

## Partner Contact for Logos

If direct downloads don't work, contact:

1. **Scania:** marketing@scania.com or check https://scania.com/press
2. **Puma:** Brand guidelines at https://about.puma.com/
3. **Danone:** Press kit at https://danone.com/media
4. **Evofenedex:** info@evofenedex.nl or check their website

## Quick Fix

The current placeholder logos (all showing Windesheim) need to be replaced. Priority order:
1. Download real Scania logo (major partner)
2. Download real Puma logo (major partner)
3. Download real Danone logo (major partner)
4. Contact Evofenedex for their logo

Once downloaded, the website will automatically show the correct logos since the HTML references are already in place.
