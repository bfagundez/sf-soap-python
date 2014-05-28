from sforce_custom.partner import SforcePartnerClient

h = SforcePartnerClient('static/partner.wsdl')
print 'Logging in...'
h.login('user','pwd','token')
print 'querying accounts'
print str(h.query('select id, Name from Account'))


