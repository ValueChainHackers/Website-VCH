# DNS Subdomain Setup Guide

## Project Subdomains Configuration

All VCH projects now use subdomains of `valuechainhackers.xyz`. This document explains how to set them up.

---

## Required Subdomains

The following subdomains need DNS configuration:

1. **lemonti**.valuechainhackers.xyz - CRM Lemonti project
2. **textile**.valuechainhackers.xyz - Textile Twicely project
3. **cacao**.valuechainhackers.xyz - Cacao Guide project
4. **bakery**.valuechainhackers.xyz - Bakery Network project
5. **cacaochain**.valuechainhackers.xyz - Cacao Chain Improvement project
6. **beerbottle**.valuechainhackers.xyz - Beer Bottle Waste Reduction project
7. **windmill**.valuechainhackers.xyz - Windmill Gearbox Niobium project
8. **phonebattery**.valuechainhackers.xyz - Phone Battery Cobalt project

---

## DNS Configuration Options

### Option 1: GitHub Pages (Recommended for Static Sites)

For each project hosted on GitHub Pages:

1. **Create CNAME file** in project repository root:
   ```
   lemonti.valuechainhackers.xyz
   ```

2. **Add DNS CNAME record** in your DNS provider:
   ```
   Type: CNAME
   Name: lemonti
   Value: valuechainhackers.github.io
   TTL: 3600
   ```

3. **Enable custom domain** in GitHub repository settings:
   - Go to Settings → Pages
   - Enter: `lemonti.valuechainhackers.xyz`
   - Check "Enforce HTTPS"

### Option 2: Wildcard Subdomain (Easiest for Multiple Projects)

If all projects point to the same server:

1. **Add wildcard CNAME record**:
   ```
   Type: CNAME
   Name: *
   Value: valuechainhackers.github.io (or your server)
   TTL: 3600
   ```

2. This allows ALL subdomains to work automatically
3. Configure routing on your web server/GitHub Pages

### Option 3: Individual CNAME Records

For projects on different servers:

```dns
lemonti.valuechainhackers.xyz    → CNAME → lemonti-project.github.io
textile.valuechainhackers.xyz    → CNAME → textile-project.github.io
cacao.valuechainhackers.xyz      → CNAME → cacao-guide.github.io
bakery.valuechainhackers.xyz     → CNAME → bakery-network.github.io
cacaochain.valuechainhackers.xyz → CNAME → cacao-chain.github.io
beerbottle.valuechainhackers.xyz → CNAME → beer-bottle.github.io
windmill.valuechainhackers.xyz   → CNAME → windmill-project.github.io
phonebattery.valuechainhackers.xyz → CNAME → phone-battery.github.io
```

---

## DNS Provider Instructions

### Cloudflare

1. Log into Cloudflare dashboard
2. Select `valuechainhackers.xyz` domain
3. Go to DNS → Records
4. Click "Add record"
5. Select Type: CNAME
6. Name: `lemonti` (or wildcard `*`)
7. Target: `valuechainhackers.github.io`
8. Proxy status: DNS only (grey cloud) for GitHub Pages
9. Click Save

### Google Domains / Google Cloud DNS

1. Go to DNS settings
2. Click "Manage custom records"
3. Add new record:
   - Host name: `lemonti`
   - Type: CNAME
   - TTL: 1h
   - Data: `valuechainhackers.github.io`
4. Save

### Other DNS Providers (Namecheap, GoDaddy, etc.)

Similar process:
1. Find DNS management section
2. Add CNAME record
3. Point to appropriate target

---

## Placeholder Solution (Until DNS is Configured)

Currently, all project links point to:
- `https://[project].valuechainhackers.xyz`

Until DNS is configured, these will show a "domain not found" error. Options:

### Temporary Fix 1: Use Placeholder Page
Redirect all subdomains to the placeholder page:
```
https://valuechainhackers.xyz/assets/documents/project-placeholder.html
```

### Temporary Fix 2: Use GitHub Repos
Point to actual GitHub repositories:
```
https://github.com/ValueChainHackers/[project-name]
```

### Temporary Fix 3: Coming Soon Page
Create a simple coming soon page hosted at main domain

---

## Project Hosting Options

Each subdomain can point to:

1. **Separate GitHub Pages repo** - Best for independent projects
   - Create repo: `ValueChainHackers/lemonti`
   - Enable GitHub Pages
   - Add CNAME file with subdomain

2. **Subdirectory in main repo** - Simpler but less flexible
   - Host at: `valuechainhackers.xyz/projects/lemonti`
   - Use redirects or routing

3. **External hosting** - For dynamic projects
   - Heroku, Vercel, Netlify, etc.
   - Point CNAME to their provided domain

4. **Quarto/Hugo subsites** - For documentation
   - Build separate sites for each project
   - Deploy to GitHub Pages

---

## Testing Subdomain Setup

After DNS configuration:

1. **Wait for DNS propagation** (can take up to 48 hours, usually < 1 hour)

2. **Check DNS with dig**:
   ```bash
   dig lemonti.valuechainhackers.xyz
   ```

3. **Test HTTPS**:
   ```bash
   curl -I https://lemonti.valuechainhackers.xyz
   ```

4. **Online tools**:
   - https://dnschecker.org
   - https://www.whatsmydns.net

---

## Recommended Approach

**For VCH Projects:**

1. ✅ Use wildcard CNAME (`*`) pointing to main GitHub Pages
2. ✅ Create routing logic in main site to handle subdomains
3. ✅ OR create separate repos for each major project
4. ✅ Use placeholder page until project sites are ready

**Quick Start (Wildcard):**
```dns
*.valuechainhackers.xyz → CNAME → valuechainhackers.github.io
```

Then all subdomains automatically resolve, and you can build out individual project pages as needed.

---

## Security Considerations

- ✅ Always enable HTTPS (free with GitHub Pages)
- ✅ Use DNS only mode (not proxied) for GitHub Pages on Cloudflare
- ✅ Add CAA records for SSL certificates
- ✅ Regular security updates for any custom code

---

## Next Steps

1. [ ] Choose DNS configuration approach (wildcard vs individual)
2. [ ] Add DNS records in domain registrar
3. [ ] Create project pages/repos for each subdomain
4. [ ] Test all subdomain links
5. [ ] Enable HTTPS for all subdomains
6. [ ] Update main website if needed

---

**Questions?** Contact Christiaan Verhoef (c.verhoef@windesheim.nl)
