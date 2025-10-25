# Global Field Listeners and Validators

You can define field-specific listeners and validators at the form level. This allows for a more centralized and organized way to manage field behavior, especially in large and complex forms.

## `fieldListeners`

The `fieldListeners` option is an object where the keys are field names and the values are listener objects. The listener objects have the same shape as the `listeners` prop on the `Field` component.

```tsx
import { useForm } from '@tanstack/react-form'

function MyForm() {
  const form = useForm({
    defaultValues: {
      firstName: '',
      lastName: '',
    },
    fieldListeners: {
      firstName: {
        onChange: ({ fieldApi }) => {
          console.log('First name changed to:', fieldApi.state.value)
        },
      },
    },
  })

  // ...
}
```

## `fieldValidators`

The `fieldValidators` option is an object where the keys are field names and the values are validator objects. The validator objects have the same shape as the `validators` prop on the `Field` component.

```tsx
import { useForm } from '@tanstack/react-form'

function MyForm() {
  const form = useForm({
    defaultValues: {
      firstName: '',
      lastName: '',
    },
    fieldValidators: {
      lastName: {
        onChange: ({ value }) =>
          value.length < 3
            ? 'Last name must be at least 3 characters'
            : undefined,
      },
    },
  })

  // ...
}
```
