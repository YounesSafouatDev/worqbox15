# Use the official Odoo image as the base
FROM odoo:15.0

# Copy custom configuration and addons
COPY ./odoo.conf /etc/odoo/odoo.conf
COPY ./addons /mnt/extra-addons

# Set permissions only if required, and avoid using `chown` in restricted environments
USER root
RUN chmod -R 755 /mnt/extra-addons /etc/odoo/odoo.conf

# Expose the Odoo service port
EXPOSE 8069

# Switch back to the default Odoo user for security
USER odoo

# Set the default command to run Odoo
CMD ["odoo"]
