# Personal Automation Utilities

Static public information for privately operated, non-commercial personal automation utilities. The only currently documented utility is **PHIS Termux Backup**.

## Structure and privacy boundary

- `/index.html`: reusable landing page
- `/phis-termux-backup/`: homepage, privacy policy, and terms
- `/assets/site.css`: the site's only stylesheet; it is self-contained and has no external dependencies
- `/google6327aedd63778de2.html`: historical Google verification file retained pending owner review
- `/scripts/validate_site.py`: dependency-free static checks

The retired Buildcon template directories (`assets/css/`, `assets/fonts/`, `assets/js/`, and `assets/sass/`) and their Creative Commons license were removed together because no current page uses or derives from those template assets. Validation requires those directories to remain absent.

Do not add health data, personal details, database content, OAuth credentials or tokens, keys, archives, private Drive identifiers, infrastructure details, analytics, forms, trackers, or automation runtime code.

## Validation

Run `python3 scripts/validate_site.py`. Static checks do **not** prove GitHub Pages availability or Google branding approval.

## Publication boundary

Pages is intended to be served from `master` only after owner review and merge. A merge does not guarantee Pages publication, domain verification, Google approval, or durable refresh tokens. Publication and Google configuration are separate owner-only actions.

### Owner-only post-publication checklist

1. Check the actual HTTPS responses for the [root](https://2harsharaj.github.io/), [app](https://2harsharaj.github.io/phis-termux-backup/), [privacy](https://2harsharaj.github.io/phis-termux-backup/privacy.html), and [terms](https://2harsharaj.github.io/phis-termux-backup/terms.html) pages.
2. Check Search Console ownership and whether Google accepts the shared GitHub Pages domain. Do not fabricate ownership proof if rejected.
3. Update Google Auth Platform Branding with verified links and attempt Publish app.
4. Separately validate any Google brand verification and refresh-token durability.
5. Consult rclone's [own client ID guidance](https://rclone.org/drive/#making-your-own-client_id).

Do not publish Pages, alter Google Cloud/OAuth, or deploy the backup utility as part of site changes.
