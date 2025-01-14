# Use the official Odoo image as the base
FROM odoo:15.0

# Install any additional dependencies (if needed)
# RUN apt-get update && apt-get install -y some-package

# Copy custom configuration and addons
COPY ./odoo.conf /etc/odoo/odoo.conf
COPY ./addons /mnt/extra-addons

# Set permissions
RUN chown -R odoo:odoo /mnt/extra-addons /etc/odoo/odoo.conf

# Expose the Odoo service port
EXPOSE 8069

# Set the default command to run Odoo
CMD ["odoo"]
