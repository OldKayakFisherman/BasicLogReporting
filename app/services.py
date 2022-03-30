from models import AnalyzerConfiguration, ConfigurationValidationResponse


class ImportValidatorService:
    def validateImport(self, conf: AnalyzerConfiguration):
        validation_response: ConfigurationValidationResponse = ConfigurationValidationResponse()

        if conf.Logs.count() is 0:
            validation_response.Messages.append("Missing audit logs for analysis")

        if conf.RequestHeaderLogField is None:
            validation_response.Messages.append("Missing request header log field identifier")

        if conf.UserIdLogField is None:
            validation_response.Messages.append("Missing user id log field identifier")

        if conf.EventTypeLogField is None:
            validation_response.Messages.append("Missing event type log field identifier")

        if conf.EventDateLogField is None:
            validation_response.Messages.append("Missing event date log field identifier")

        if conf.RemoteAddressLogField is None:
            validation_response.Messages.append("Missing remote address log field identifier")

        validation_response.IsValid = validation_response.Messages.count() > 0

        return validation_response
