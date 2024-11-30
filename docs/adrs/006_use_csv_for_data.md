# Use CSV Files as Data Source with File Upload Functionality

## Status

Accepted

## Context

For our application, we needed a convenient and straightforward way to manage and process data. CSV files provide a lightweight and widely-used format for data storage and exchange. To enhance user convenience, we also decided to allow users to upload CSV files directly.

The following considerations were taken into account:

- **Simplicity:** CSV files are easy to create, edit, and use with standard tools like spreadsheets.
- **Use Case:** The system is intended for use by a single person on a local machine, minimizing complexity and operational overhead.
- **Security Risk:** While file uploads inherently carry some security risks, the intended local usage scenario significantly mitigates these risks.

## Decision

We have decided to use **CSV files** as the primary data source and enable file uploads for convenience. The reasons for this decision are:

1. **Ease of Use:** CSV files are easy to handle, allowing users to manage data without specialized knowledge or tools.
2. **Compatibility:** CSV files are supported by nearly all data tools and programming libraries, ensuring seamless integration.
3. **Lightweight Format:** CSV is a simple text-based format with minimal overhead, making it efficient for local use cases.
4. **Convenience of Uploads:** Allowing file uploads simplifies data entry and enables users to quickly import data without manual input.
5. **Risk Mitigation Through Intended Use:** The application is expected to be used by a single person on a local machine, reducing exposure to potential file upload security risks.

## Consequences

### Positive

- **User-Friendly:** Users can easily manage and upload their data using familiar tools.
- **Simplicity:** The lightweight nature of CSV files reduces complexity in data handling and storage.
- **Performance:** Processing small CSV files locally ensures fast and efficient operation.

### Negative

- **Limited Scalability:** CSV files are not ideal for large-scale or multi-user environments.
- **Potential for Errors:** Manual handling of CSV files may introduce formatting errors or inconsistencies.
- **Security Risks (Mitigated):** While file uploads could introduce risks, the intended single-user, local scenario significantly reduces this concern. However, misuse outside the intended use case could pose a risk.

## Follow-Up Actions

1. **Validation on Upload:** Implement validation to ensure uploaded CSV files adhere to the expected format and structure.
2. **Error Handling:** Provide clear error messages for formatting issues or invalid data.
3. **Documentation:** Clearly document the intended usage scenario and limitations to avoid misuse.
4. **Optional Enhancements:** Explore adding checks for file size or type to further mitigate potential misuse.
5. **Monitor Feedback:** Gather user feedback to determine if the current approach meets their needs or requires adjustments.

## Alternatives Considered

- **Database Storage:** Provides scalability and multi-user support but introduces additional complexity not required for the intended single-user use case.
- **JSON Files:** More structured than CSV but less user-friendly for non-technical users and not as widely supported by common tools.
- **Online Uploads:** Allowing uploads in a multi-user environment would require significant security measures, which are unnecessary for the current scope.

## Summary

Using CSV files as the data source with file upload functionality provides a simple, user-friendly, and efficient solution for the intended single-user, local use case. While there are inherent risks with file uploads, the local usage scenario mitigates these risks effectively. This approach aligns with the project’s goals of simplicity and convenience while keeping security considerations in check.
